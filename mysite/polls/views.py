from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from polls.products import Products


def index(request):
    return render(request, "index.html", {})


def cardapio(request):
    products = Products().getAllProducts()
    print(products)
    context = {"products": products}
    return render(request, "products.html", context)
