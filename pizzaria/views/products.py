from django.shortcuts import render
from pizzaria.controller.products import Products
from pizzaria.controller.categories import Categories
import pizzaria.views.templates as templates


def all(request):
    categories = Categories().all()
    searched_category = None
    products = []
    if request.GET and request.GET.get("category"):
        category = request.GET.get("category")
        if category in [c.name for c in categories]:
            searched_category = category
            products = Products().perCategory(category=category)
    else:
        products = Products().all()
    context = {
        "products": products,
        "categories": categories,
        "searched_category": searched_category,
    }
    return render(request, templates.PRODUCTS, context)
