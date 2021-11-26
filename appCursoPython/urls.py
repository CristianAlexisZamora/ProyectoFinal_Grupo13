from django.urls import path

# Importando views de la aplicacion main
from appCursoPython import views

urlpatterns = [
    path('POO/', views.pythonPOO, name="POO"),
    path('tutorial01/', views.cursoDjango01, name="FrameworkDjango01"),
    path('tutorial02/', views.cursoDjango02, name="FrameworkDjango02"),
    path('libros/', views.listado_libros, name="Libros"),
    path('videosComplementarios/', views.videosComplementarios, name="VideosComplementarios"),
    path('operadores/', views.operadores, name="Operadores"),
]