from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'sexo',
                'edad',
                'last_name',
                'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email' : 'Correo',
            'sexo': 'Sexo',
            'edad': 'Edad',

        }