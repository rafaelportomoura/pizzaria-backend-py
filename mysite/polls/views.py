from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from polls.services.products import ProductsService
from polls.services.orders import OrderService


def index(request):
    return render(request, "index.html", {})


def cardapio(request):
    products = ProductsService().getAllProducts()
    print(products)
    context = {"products": products}
    return render(request, "products.html", context)


def cart(request):
    cart = OrderService().getCartOrder()
    return cart
