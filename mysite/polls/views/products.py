from django.shortcuts import render
from polls.controller.products import Products
import polls.views.templates as templates


def all(request):
    products = Products().getAllProducts()
    context = {"products": products}
    return render(request, templates.PRODUCTS, context)
