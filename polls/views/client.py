import polls.views.templates as templates
from django.shortcuts import render, redirect
from polls.controller.client import ClientController, ClientError


def client(request):
    try:
        if request.method == "GET":    
            return render(request, templates.CLIENT, {})
        elif request.method == "POST":
            ClientController().register(request)
            print(request.POST)
            return redirect("index")
    except ClientError as e:
        context = {"error": e.message}
        return render(request, templates.CLIENT, context)
    except Exception as e:
        print(e)
        context = {"error": "Erro inesperado!"}
        return render(request, templates.CLIENT, context)

