from django.shortcuts import render
from polls.controller.orders import OrderService
import polls.views.templates as templates
from django.contrib.auth.decorators import login_required


@login_required
def all(request):
    orders = OrderService().all()
    
    context = {
        "orders": orders,
    }
    return render(request, templates.ORDERS, context)
