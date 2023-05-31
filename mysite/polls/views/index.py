from django.shortcuts import render
import polls.views.auth as auth
import polls.views.products as products
import polls.views.templates as templates


def index(request):
    return render(request, templates.INDEX, {})
