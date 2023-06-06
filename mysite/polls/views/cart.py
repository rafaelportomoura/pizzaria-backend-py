from django.shortcuts import render
import polls.views.templates as templates
from django.contrib.auth.decorators import login_required
from polls.controller.cart import CartController
from django.http import HttpResponse


@login_required
def cart(request):
    context = {}
    cart, items, total = CartController(request.user).getCart()
    if cart:
        context["cart"] = items
        context["total"] = total

    return render(request, templates.CART, context)


@login_required
def add(request, product_id):
    CartController(request.user).addItem(product_id)
    return HttpResponse('{"message": "Adicionado com sucesso"}')


@login_required
def remove(request, product_id):
    CartController(request.user).removeItem(product_id)
    return HttpResponse('{"message": "Adicionado com sucesso"}')
