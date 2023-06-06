from polls.controller.auth import Auth
from polls.models import Cart, CartItem
from polls.controller.products import Products


class CartController:
    def __init__(self, user):
        self.client = Auth().isClient(user=user)

    def getCart(self):
        if not self.client:
            return None, None

        cart = self.client.cart

        if not cart:
            return None, None

        items = cart.cartitem_set.all()

        total = 0
        for item in items:
            item.total_price = item.quantity * item.product.price
            total = total + item.total_price

        return cart, items, total

    def addItem(self, product_id):
        if not self.client:
            raise Exception("O usuário não é um cliente!")

        product = Products().getById(product_id)

        cart = self.client.cart

        items = cart.cartitem_set.all()
        for item in items:
            if int(item.product.id) == int(product_id):
                item.quantity = item.quantity + 1
                item.save()
                return True

        CartItem.objects.create(product=product, cart=cart, quantity=1)

    def removeItem(self, product_id):
        if not self.client:
            raise Exception("O usuário não é um cliente!")

        cart = self.client.cart

        items = cart.cartitem_set.all()
        for item in items:
            if int(item.product.id) == int(product_id):
                item.quantity = item.quantity - 1
                if item.quantity == 0 or item.quantity < 0:
                    item.delete()
                else:
                    item.save()
                return True
        return False
