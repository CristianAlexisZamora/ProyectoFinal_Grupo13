from django.shortcuts import render
from appCursoPython.models import practica
# Create your views here.
# Vista creada para la pagina de POO en python
def pythonPOO(request):
    return render(request, "appCursoPython/pythonPOO.html")

# Vistas creadas para el curso del framework Django
def cursoDjango01(request):
    return render(request, "django/cursoDjango01.html")

def cursoDjango02(request):
    return render(request, "django/cursoDjango02.html")

def cursoDjango03(request):
    return render(request, "django/cursoDjango03.html")

def cursoDjango04(request):
    return render(request, "django/cursoDjango04.html")

# Vista creada para el listado de libros que se posee
def listado_libros(request):
    return render(request, "appCursoPython/libros.html")

#Vista de la pagina principal de videos complementarios
def videosComplementarios(request):
    return render(request, "appCursoPython/videosComplementarios.html")

#Vista de la pagina principal de Comunidad
def comunidad (request):
    return render(request, "appCursoPython/comunidad.html")

# Vista creada para el tutorial de Operadores
def operadores(request):
    return render(request, "appcursoPython/operadores.html")

# Vista creada para el tutorial de sentencia if
def sentenciaIf(request):
    return render(request, "appcursoPython/sentenciaIf.html")

# Vista creada para el tutorial de sentencia if
def bucleWhile(request):
    return render(request, "appcursoPython/bucleWhile.html")

#Vista creada para la práctica
def practicapage(request, modulo):
    resultado = practica.objects.get(idpractica=modulo)
    return render(request, "appcursoPython/practica.html", {"tema":resultado.tema, "pregunta1":resultado.pregunta1, "pregunta2":resultado.pregunta2, "pregunta3":resultado.pregunta3})

<<<<<<< HEAD
=======
#Vista creada para el tutorial de introduccion a python
def introduccion(request):
    return render(request, "appcursoPython/introduccion.html")

#Vista creada para el tutorial de variables
def variables(request):
    return render(request, "appcursoPython/variables.html")
>>>>>>> origin/main
#Modulo 3

# Vista creada para el tutorial de tipoRange
def tipoRange(request):
    return render(request, "appCursoPython/tipoRange.html")
# Vista creada para el tutorial de tipoSet
def tipoSet(request):
    return render(request, "appCursoPython/tipoSet.html")
# Vista creada para el tutorial de tipoDict
def tipoDict(request):
<<<<<<< HEAD
    return render(request, "appCursoPython/tipoDict.html")
=======
    return render(request, "appCursoPython/tipoDict.html")

#Vista creada para el tutorial de tipos de datos
def tiposDatos(request):
    return render(request, "appCursoPython/tiposDatos.html")
>>>>>>> origin/main
