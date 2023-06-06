from django.contrib.auth import authenticate, login
from urllib.parse import parse_qsl
from polls.models import Client


class AuthError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Erro de Autenticação: {self.message}"


class Auth:
    def __init__(self, request=None):
        self.request = request

    def login(self):
        body = dict(parse_qsl(self.request.body.decode("utf-8")))
        user = authenticate(
            request=self.request, username=body["username"], password=body["password"]
        )
        if user == None:
            raise AuthError("Usuário ou senha inválidos!")

        if not self.isClient(user):
            raise AuthError("Usuário não tem acesso como cliente!")

        login(request=self.request, user=user)
        return user

    def isClient(self, user):
        try:
            client = Client.objects.get(user_id=user)
            return client
        except:
            return False
