from django.urls import path

# Importando views de la aplicacion main
from appCursoPython import views

urlpatterns = [
    path('POO/', views.pythonPOO, name="POO"),
    path('cursoDjango/', views.cursoDjango01, name="FrameworkDjango"),
    path('ejercicioDjango/', views.cursoDjango02, name="EjercicioDjango"),
    path('libros/', views.listado_libros, name="Libros"),
    path('videosComplementarios/', views.videosComplementarios, name="VideosComplementarios"),
    path('operadores/', views.operadores, name="Operadores"),
]