from django.contrib import admin
from .models import Category, Client, Order, Product, Cart, CartItem, OrderItem


admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
