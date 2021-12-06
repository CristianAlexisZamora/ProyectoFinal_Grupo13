from django.shortcuts import render, redirect
from appCursoPython.models import practica

#--------------------Modulo 1 ------------------------#
#Vista para el tutorial de introduccion
def introduccion(request):
    return render(request, "appCursoPython/introduccion.html")

#Vista para el tutorial de tipos de datos
def variables(request):
    return render(request, "appCursoPython/variables.html")

#Vista para el tutorial de variables
def tiposDatos(request):
    return render(request, "appCursoPython/tiposDatos.html")

# Vista creada para el tutorial de Operadores
def operadores(request):
    return render(request, "appcursoPython/operadores.html")
   

#------------------- Modulo 2 ------------------------#
# Vista creada para el tutorial de sentencia if
def sentenciaIf(request):
    return render(request, "appcursoPython/sentenciaIf.html")

# Vista creada para el tutorial de sentencia if
def bucleWhile(request):
    return render(request, "appcursoPython/bucleWhile.html")

def bucleFor(request):
    return render(request, "appcursoPython/bucleFor.html")

#------------------ Modulo 3 -------------------------#
#vista creada para el tutorial de tipo List
def tipoList(request):
    return render(request, "appcursoPython/tipoList.html")
# Vista creada para el tutorial de tipoRange
def tipoRange(request):
    return render(request, "appCursoPython/tipoRange.html")
# Vista creada para el tutorial de tipoSet
def tipoSet(request):
    return render(request, "appCursoPython/tipoSet.html")
# Vista creada para el tutorial de tipoDict
def tipoDict(request):
    return render(request, "appCursoPython/tipoDict.html")
# Vista creada para el tutorial de tipoStr
def tipoStr(request):
    return render(request, "appCursoPython/tipoStr.html")


#----------------- Modulo 4 ---------------------------#
# Vista creada para el tutorial de funciones en python
def funciones(request):
    return render(request, "appCursoPython/funciones.html")
# Vista creada para el tutorial de Espacios de nombres, modulos y paquetes
def espacioNombres(request):
    return render(request, "appCursoPython/Espaciosnmp.html")
# Vista creada para el tutorial de programacion orientada a objetos
def pythonPOO(request):
    return render(request, "appCursoPython/pythonPOO.html")


#----------------Django---------------------------------#
# Vistas creadas para el curso del framework Django
def cursoDjango01(request):
    return render(request, "django/cursoDjango01.html")

def cursoDjango02(request):
    return render(request, "django/cursoDjango02.html")

def cursoDjango03(request):
    return render(request, "django/cursoDjango03.html")

def cursoDjango04(request):
    return render(request, "django/cursoDjango04.html")



#------------------ Otras vistas ------------------------#
# Vista creada para el tutorial de inicio
def inicio(request):
    return render(request, "appCursoPython/inicio.html") 

# Vista creada para el listado de libros que se posee
def listado_libros(request):
    return render(request, "appCursoPython/libros.html")

#Vista de la pagina principal de videos complementarios
def videosComplementarios(request):
    return render(request, "appCursoPython/videosComplementarios.html")

#Vista de la pagina principal de Comunidad
def comunidad (request):
    return render(request, "appCursoPython/comunidad.html")

#Vista creada para la práctica
def practicapage(request, modulo):
    resultado = practica.objects.get(idpractica=modulo)
    return render(request, "appcursoPython/practica.html", {"modulo":resultado.idpractica,"tema":resultado.tema, "pregunta1":resultado.pregunta1, "pregunta2":resultado.pregunta2, "pregunta3":resultado.pregunta3, "res1":resultado.respuesta1, "res2":resultado.respuesta2, "res3":resultado.respuesta3})
