from django.urls import path
#from ProyectoFinal_Grupo13 import views
# Importando views de la aplicacion main
from main import views

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('libros/', views.listado_libros, name="Libros"),
    path('videosComplementarios/', views.videosComplementarios, name="VideosComplementarios"),
    path('academia/', views.academiaCurso, name="AcademiaCurso"),
]