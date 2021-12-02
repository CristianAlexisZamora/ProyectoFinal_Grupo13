from django.db import models

# Create your models here.
class usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=30, null=False)
    premium = models.BooleanField()

class practica(models.Model):
    idpractica = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30,null=False)
    pregunta1 = models.CharField(max_length=160)
    pregunta2 = models.CharField(max_length=160)
    pregunta3 = models.CharField(max_length=160)
    respuesta1 = models.CharField(max_length=80, default="")
    respuesta2 = models.CharField(max_length=80, default="")
    respuesta3 = models.CharField(max_length=80, default="")
    