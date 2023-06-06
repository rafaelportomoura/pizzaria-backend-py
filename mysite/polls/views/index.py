from django.shortcuts import render
import polls.views.auth as auth
import polls.views.products as products
import polls.views.templates as templates
import polls.views.cart as cart
import polls.views.client as client
import polls.views.orders as orders


def index(request):
    return render(request, templates.INDEX, {})
