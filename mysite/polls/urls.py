from django.urls import path
import polls.views.index as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos", views.products.all, name="produtos"),
    path("login", views.auth.login, name="login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)
