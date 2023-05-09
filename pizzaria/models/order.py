from django.db import models
from models.client import Client
from models.employee import Employee


class Order(models.Model):
    status_choice = [
        (0, "Cancelled"),
        (1, "Placed"),
        (2, "Processing"),
        (3, "Completed"),
    ]
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    employee = models.ForeignKey(
        Employee, null=True, blank=True, on_delete=models.RESTRICT
    )
    status = models.IntegerField(max_length=2, choices=status_choice, default=1)
    datetime = models.DateField(auto_now_add=True)
