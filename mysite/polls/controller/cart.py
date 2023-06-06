from polls.controller.auth import Auth
from polls.models import Cart


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

        return items, total
