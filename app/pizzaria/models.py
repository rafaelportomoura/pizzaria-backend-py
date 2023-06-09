from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User
import time
from django.db.models.signals import post_save
from django.dispatch import receiver


def filepath(table, instance, filename):
    epoch = int(time.time())
    return f"{table}/{instance.name}/{epoch}_{filename}"


def product_file_path(instance, filename):
    return filepath("product", instance, filename)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    status_choice = [
        (0, "INACTIVE"),
        (1, "ACTIVE"),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=80)
    created_at = models.TimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choice, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    status_choice = [(0, "Lacking"), (1, "Available")]
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    picture = models.ImageField(
        upload_to=product_file_path,
    )
    status = models.IntegerField(choices=status_choice, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    status_choice = [
        (0, "Cancelado"),
        (1, "Pedido Realizado"),
        (2, "Preparando"),
        (3, "Completo"),
    ]
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    employee = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.RESTRICT, default=None
    )
    status = models.IntegerField(choices=status_choice, default=1)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product}"


class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.client.__str__()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} (Quantity: {self.quantity})"


@receiver(post_save, sender=Client)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(client=instance)
