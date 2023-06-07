from django.shortcuts import render, redirect
from polls.controller.orders import OrderService
import polls.views.templates as templates
from django.contrib.auth.decorators import login_required


@login_required
def all(request):
    orders, total = OrderService().all(request=request)

    context = {"orders": orders, "total": total}
    return render(request, templates.ORDERS, context)


@login_required
def create_order(request):
    if request.method == "POST":
        order, items, total = OrderService().create(request)

        return render(
            request,
            templates.ORDER_CREATED,
            {"order": order, "items": items, "total": total},
        )

    return redirect("orders")
