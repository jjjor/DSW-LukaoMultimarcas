from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = 'pages/index.html'

class LoginView(TemplateView):
    template_name = 'pages/login.html'