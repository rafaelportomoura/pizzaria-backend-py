from django.shortcuts import render, redirect
from pizzaria.controller.auth import Auth, AuthError
import pizzaria.views.templates as templates
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login(request):
    try:
        if request.method == "GET":
            return render(request, templates.LOGIN, {})
        elif request.method == "POST":
            login_service = Auth(request=request)
            user = login_service.login()
            print(request.POST)
            return redirect("index")
    except AuthError as e:
        context = {"error": e.message}
        return render(request, templates.LOGIN, context)
    except Exception as e:
        print(e)
        context = {"error": "Erro inesperado!"}
        return render(request, templates.LOGIN, context)


@login_required
def logout_view(request):
    print(request)
    logout(request)
    return redirect("index")
