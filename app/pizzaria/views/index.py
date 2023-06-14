from django.shortcuts import render
import pizzaria.views.auth as auth
import pizzaria.views.products as products
import pizzaria.views.templates as templates
import pizzaria.views.cart as cart
import pizzaria.views.client as client
import pizzaria.views.orders as orders


def index(request):
    return render(request, templates.INDEX, {})
