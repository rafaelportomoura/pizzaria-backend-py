import polls.views.templates as templates
from django.shortcuts import render
from polls.controller.client import ClientController, ClientError


def client(request):
    try:
        if request.method == "GET":    
            return render(request, templates.CLIENT, {})
        elif request.method == "POST":
            ClientController().register(request)
            return render(request, templates.CLIENT, {})
    except Exception as e:
        print(e)
        context = {"error": "Erro inesperado!"}
        return render(request, templates.CLIENT, context)

