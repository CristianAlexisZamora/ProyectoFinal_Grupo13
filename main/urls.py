from django.urls import path, include
#from ProyectoFinal_Grupo13 import views
# Importando views de la aplicacion main
from main import views
from django.conf.urls import url

urlpatterns = [
    path('academia/', views.academiaCurso, name="AcademiaCurso"),
    path('cuenta/', views.cuenta, name="Cuenta"),
    path('nosotros/', views.nosotros, name="Nosotros"),
]