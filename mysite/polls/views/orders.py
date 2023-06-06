from django.shortcuts import render
from polls.controller.orders import OrderService
import polls.views.templates as templates


def all(request):
    orders = OrderService().all()
    context = {
        "orders": orders,
    }
    return render(request, templates.ORDERS, context)
