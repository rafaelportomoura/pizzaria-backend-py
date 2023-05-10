from django.db import models
from datetime import datetime
from django.contrib import admin
import time

MEDIA_ROOT = "media/polls"


def filepath(table, instance, filename):
    epoch = int(time.time())
    return f"{MEDIA_ROOT}/{table}/{instance.id}/{epoch}_{filename}"


def category_file_path(instance, filename):
    return filepath("category", instance, filename)


def product_file_path(instance, filename):
    return filepath("product", instance, filename)


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()
    picture = models.ImageField(upload_to=category_file_path)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=80)
    created_at = models.CharField(max_length=27)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="ACTIVE")

    def __str__(self):
        return f"{name} {last_name}"


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
    status = models.IntegerField(choices=status_choice, default=1)
    datetime = models.DateField(auto_now_add=True)


class Product(models.Model):
    status_choice = [(0, "Lacking"), (1, "Available")]
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    picture = models.ImageField(
        upload_to=product_file_path,
    )
    status = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return self.name


# class GroupInLine(admin.TabularInline):
#     model = Group

# class EmployeeInLine(admin.ModelAdmin):
# inlines = [ GroupInLine]

# admin.site.register(Employee, EmployeeInLine)
