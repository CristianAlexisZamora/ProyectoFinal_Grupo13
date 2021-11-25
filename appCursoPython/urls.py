from django.urls import path

# Importando views de la aplicacion main
from appCursoPython import views

urlpatterns = [
    path('POO/', views.pythonPOO, name="POO"),
    path('cursoDjango/', views.frameworkDjango, name="FrameworkDjango"),
    path('ejercicioDjango/', views.ejercicioDjango, name="EjercicioDjango"),
    path('libros/', views.listado_libros, name="Libros"),
    path('videosComplementarios/', views.videosComplementarios, name="VideosComplementarios"),
]