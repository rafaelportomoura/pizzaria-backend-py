from django.urls import path

import polls.views.index as views

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos", views.products.all, name="produtos"),
    path("login", views.auth.login, name="login"),
]
