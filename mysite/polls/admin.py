from django.contrib import admin
from .models import Category, Client, Order, Product


admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
