from django.shortcuts import render

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


# Vista creada para el tutorial de Operadores
def operadores(request):
    return render(request, "appcursoPython/operadores.html")

# Vista creada para el tutorial de sentencia if
def sentenciaIf(request):
    return render(request, "appcursoPython/sentenciaIf.html")

# Vista creada para el tutorial de sentencia if
def bucleWhile(request):
    return render(request, "appcursoPython/bucleWhile.html")
