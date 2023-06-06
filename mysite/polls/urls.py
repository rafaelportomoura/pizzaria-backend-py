from django.urls import path, re_path
import polls.views.index as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^produtos/?$", views.products.all, name="produtos"),
    re_path(r"^login/?$", views.auth.login, name="login"),
    re_path(r"^cart/?$", views.cart.cart, name="cart"),
    re_path(
        r"^cart/(?P<product_id>\d+)/add/?$", views.cart.add, name="cart_product_add"
    ),
    re_path(r"^sair/?$", views.auth.logout_view, name="logout"),
    re_path(r"^cliente/?$", views.client.client, name="client"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
