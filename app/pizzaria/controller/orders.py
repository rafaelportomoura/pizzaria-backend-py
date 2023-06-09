import json
from urllib.parse import parse_qsl

from django.forms.models import model_to_dict
from pizzaria.controller.auth import Auth
from pizzaria.controller.cart import CartController
from pizzaria.models import Order, OrderItem
from pizzaria.providers.rabbitmq import RabbitMQ


class OrderService:
    def __init__(self) -> None:
        self.model = Order
        self.status_choice = {}
        for status in Order.status_choice:
            value, key = status
            self.status_choice[value] = key
        self.rabbitmq = RabbitMQ()

    def all(self, request):
        user = request.user
        client = Auth().isClient(user=user)
        orders = self.model.objects.order_by("-datetime").filter(client=client)
        total = 0
        for order in orders:
            order, order_items, order_total = self.getOrderWithTotalAndStatus(order)
            order.items = order_items
            order.datetime = order.datetime.strftime("%d/%m/%Y")
            order.total_price = order_total
            total = total + order_total

        return orders, total

    def getOrderWithTotalAndStatus(self, order):
        items = order.orderitem_set.all()
        order.status = order.get_status_display()
        total = 0
        for item in items:
            item.total_price = item.quantity * item.product.price
            total = total + item.total_price
        return order, items, total

    def get_by_id(self, id):
        order = self.model.objects.get(id=id)
        return self.getOrderWithTotalAndStatus(order)

    def create(self, request):
        user = request.user
        client = Auth().isClient(user=user)

        if not client:
            raise Exception("Usuário não é cliente!")

        _, cart_items, total = CartController(user=user).getCart()

        if len(cart_items) <= 0:
            raise Exception("Sem itens no carrinho!")

        order = Order.objects.create(client=client)

        order.status = order.get_status_display()
        order_items = []
        for item in cart_items:
            product = item.product
            quantity = item.quantity
            order_item = OrderItem.objects.create(
                order=order, product=product, quantity=quantity
            )
            order_item.total_price = item.total_price
            order_items.append(order_item)
            item.delete()

        message_queue = json.dumps(
            {
                "order": model_to_dict(order),
                "order_items": [
                    model_to_dict(order_item) for order_item in order_items
                ],
                "total": total.__str__(),
            }
        )

        self.rabbitmq.connect()
        self.rabbitmq.send_to_queue(
            queue="order", message=message_queue, routing_key="order"
        )
        self.rabbitmq.disconnect()

        return order, order_items, total
