from django.contrib.auth import authenticate, login


class Login:
    def __init__(self, request):
        self.request = request

    def login(self):
        body = self.request.body.decode("utf-8").split("&")
        body = {key: value for [key, value] in [x.split("=") for x in body]}
        username = body["username"]
        password = body["password"]
        user = authenticate(request=self.request, username=username, password=password)
        if user == None:
            raise Exception("Invalid credentials")
        # TODO Criar verificação para ver se é cliente
        login(request=self.request, user=user)
        return user

    def session(self, user):
        self.request.session["user"] = user
