from django.shortcuts import render
from polls.controller.products import Products
from polls.controller.categories import Categories
import polls.views.templates as templates


def all(request):
    categories = Categories().all()
    products = Products().all()
    context = {"products": products, "categories": categories}
    return render(request, templates.PRODUCTS, context)
