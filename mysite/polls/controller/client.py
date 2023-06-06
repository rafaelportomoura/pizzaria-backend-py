from urllib.parse import parse_qsl
from django.contrib.auth import login
from polls.models import Client
from django.contrib.auth.models import User



class ClientError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Erro de Registro: {self.message}"
    

class ClientController:
    def register(self, request):
        
        try:
            body = dict(parse_qsl(request.body.decode("utf-8")))
            
        
            user = User.objects.create_user(body["username"], body["email"], body["password"])
                        
            Client.objects.create(user_id=user, first_name=body["first_name"], last_name=body["last_name"])
            
            login(request=request, user=user)
        
        except Exception as e:
            raise ClientError(f"Erro ao criar usuário! {e}")
        
        
        
      