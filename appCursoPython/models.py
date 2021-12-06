from django.db import models
from main.user.models import User

# Create your models here.
class usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=30, null=False)
    premium = models.BooleanField()

class practica(models.Model):
    idpractica = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=40,null=False)
    pregunta1 = models.TextField()
    pregunta2 = models.TextField()
    pregunta3 = models.TextField()
    respuesta1 = models.CharField(max_length=80, default="")
    respuesta2 = models.CharField(max_length=80, default="")
    respuesta3 = models.CharField(max_length=80, default="")
    
class nota(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_practica = models.ForeignKey('Practica', on_delete=models.CASCADE)
    nota_practica = models.FloatField(null=True)