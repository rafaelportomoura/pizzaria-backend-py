from django.shortcuts import render
from polls.controller.auth import Auth, AuthError
import polls.views.templates as templates


def login(request):
    try:
        if request.method == "GET":
            return render(request, templates.LOGIN, {})
        elif request.method == "POST":
            login_service = Auth(request=request)
            login_service.login()
            return render(request, templates.WORK_IN_PROGRESS, {})
    except AuthError as e:
        context = {"error": e.message}
        return render(request, templates.LOGIN, context)
    except Exception as e:
        print(e)
        context = {"error": "Erro inesperado!"}
        return render(request, templates.LOGIN, context)
