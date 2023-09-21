from django.urls import path

#importar views
from .views import PaginaInicial, LoginView

#tem que ser urlpatterns pq é padrão do django
urlpatterns = [
    path('', PaginaInicial.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login")
]