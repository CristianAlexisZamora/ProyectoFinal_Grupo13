from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.user.forms import RegistroForm
from main.user.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "main/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login/')