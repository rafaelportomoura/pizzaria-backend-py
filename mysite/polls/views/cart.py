from django.shortcuts import render
import polls.views.templates as templates
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    context = {}
    return render(request, templates.CART, context)
