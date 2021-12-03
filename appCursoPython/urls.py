from django.urls import path

# Importando views de la aplicacion main
from appCursoPython import views

urlpatterns = [
    path('POO/', views.pythonPOO, name="POO"),
    path('tutorial01/', views.cursoDjango01, name="FrameworkDjango01"),
    path('tutorial02/', views.cursoDjango02, name="FrameworkDjango02"),
    path('tutorial03/', views.cursoDjango03, name="FrameworkDjango03"),
    path('tutorial04/', views.cursoDjango04, name="FrameworkDjango04"),
    path('libros/', views.listado_libros, name="Libros"),
    path('videosComplementarios/', views.videosComplementarios, name="VideosComplementarios"),
    path('comunidad/', views.comunidad, name="comunidad"),
    path('operadores/', views.operadores, name="Operadores"),
    path('sentenciaIf/', views.sentenciaIf, name="SentenciaIf"),
    path('bucleWhile/', views.bucleWhile, name="BucleWhile"),
    path('practica/<int:modulo>', views.practicapage),
<<<<<<< HEAD
    path('tipoRange/', views.tipoRange, name="TipoRange"),
    path('tipoSet/', views.tipoSet, name="TipoSet"),
    path('tipoDict/', views.tipoDict, name="TipoDict"),
=======
    path('introduccion/', views.introduccion, name="Introduccion"),
    path('variables/', views.variables, name="Variables"),
    path('tipoRange/', views.tipoRange, name="TipoRange"),
    path('tipoSet/', views.tipoSet, name="TipoSet"),
    path('tipoDict/', views.tipoDict, name="TipoDict"),
    path('tiposDatos/', views.tiposDatos, name="TiposDatos"),
>>>>>>> origin/main
]