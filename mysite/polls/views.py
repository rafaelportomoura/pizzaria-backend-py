from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from polls.services.products import ProductsService
from polls.services.orders import OrderService
from polls.services.login import Login


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


def login(request):
    try:
        if request.method == "GET":
            return render(request, "login.html", {})
        elif request.method == "POST":
            login_service = Login(request=request)
            login_service.login()
            return render(request, "work_in_progress.html", {})
    except:
        context = {"error": "Login inválido!"}
        return render(request, "login.html", context)
