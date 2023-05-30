from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cardapio", views.cardapio, name="cardapio"),
    path("login", views.login, name="login"),
]
