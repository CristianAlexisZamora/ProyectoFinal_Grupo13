from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    premium = models.BooleanField(default=False)
    edad = models.DecimalField(decimal_places=0, max_digits=2,null=True)
    sexo = models.CharField(max_length=10,null=True)
