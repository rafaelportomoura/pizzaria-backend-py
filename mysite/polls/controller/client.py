from urllib.parse import parse_qsl

class ClientError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Erro de Registro: {self.message}"
    

class ClientController:
    
    def register(self, request):
        body = dict(parse_qsl(request.body.decode("utf-8")))
        print(body)
        