from django.urls import path

# Importando views de la aplicacion main
from appCursoPython import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
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
    path('bucleFor/', views.bucleFor, name="BucleFor"),
    path('practica/<int:modulo>', views.practicapage),
    path('tipoList/', views.tipoList, name="TipoList"),
    path('tipoTuple/', views.tipoTuple, name="TipoTuple"),
    path('tipoRange/', views.tipoRange, name="TipoRange"),
    path('tipoSet/', views.tipoSet, name="TipoSet"),
    path('tipoDict/', views.tipoDict, name="TipoDict"),
    path('tipoStr/', views.tipoStr, name="TipoStr"),
    path('funciones/', views.funciones, name="Funciones"),
    path('espaciosNombres/', views.espacioNombres, name="Espacionmp"),
    path('introduccion/', views.introduccion, name="Introduccion"),
    path('variables/', views.variables, name="Variables"),
    path('tiposDatos/', views.tiposDatos, name="TiposDatos"),
]