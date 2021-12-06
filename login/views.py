from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Iniciar Sesión'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Inicio')
        return super().dispatch(request, *args, **kwargs)