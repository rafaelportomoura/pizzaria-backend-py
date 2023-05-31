from polls.models import Order
from django.db import connection


class OrderService:
    def __init__(self):
        self.model = Order
        self.status_choice = {}
        for status in Order.status_choice:
            value, key = status
            self.status_choice[key] = value
