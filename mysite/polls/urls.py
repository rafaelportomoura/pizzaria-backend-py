from django.urls import path
import polls.views.index as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos", views.products.all, name="produtos"),
    path("produtos/", views.products.all, name="produtos"),
    path("login", views.auth.login, name="login"),
    path("login/", views.auth.login, name="login"),
    path("cart", views.cart.cart, name="cart"),
    path("cart/", views.cart.cart, name="cart"),
    path("sair", views.auth.logout_view, name="logout"),
    path("sair/", views.auth.logout_view, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)
