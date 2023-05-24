from polls.models import Order
from django.db import connection


class OrderService:
    def __init__(self):
        self.model = Order
        self.status_choice = {}
        for status in Order.status_choice:
            value, key = status
            self.status_choice[key] = value

    def getCartOrder(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM orders")

            orders = dictfetchall(cursor)
        return orders
        # return self.model.objects.get(status=self.status_choice["Cart"])
