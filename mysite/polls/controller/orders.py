from polls.models import Order, OrderItem
from django.db import connection
from urllib.parse import parse_qsl
from polls.controller.cart import CartController
from polls.controller.auth import Auth


class OrderService:
    def __init__(self):
        self.model = Order
        self.status_choice = {}
        for status in Order.status_choice:
            value, key = status
            self.status_choice[value] = key

    def all(self):
        orders = self.model.objects.all().order_by("datetime")
        for order in orders:
            order.status = order.get_status_display()

        return orders

    def get_by_id(self, id):
        order = self.model.objects.get(id=id)
        items = order.orderitem_set.all()
        total = 0
        for item in items:
            item.total_price = item.quantity * item.product.price
            total = total + item.total_price
        order.status_display = self.status_choice[order.status]
        return order, items, total

    def create(self, request):
        user = request.user
        client = Auth().isClient(user=user)

        if not client:
            raise Exception("Usuário não é cliente!")

        cart, items, total = CartController(user=user).getCart()

        if len(items) <= 0:
            raise Exception("Sem items para cadastrar")

        order = Order.objects.create(client=client)

        order.status_display = self.status_choice[order.status]
        order_items = []
        for item in items:
            product = item.product
            quantity = item.quantity
            order_item = OrderItem.objects.create(
                order=order, product=product, quantity=quantity
            )
            order_items.append(order_item)
            item.delete()

        return order, order_items, total
