from django.shortcuts import render

# Create your views here.
# Vista creada para la pagina de POO en python
def pythonPOO(request):
    return render(request, "appCursoPython/pythonPOO.html")

# Vista creada para el curso del framework Django
def cursoDjango01(request):
    return render(request, "appCursoPython/cursoDjango01.html")

# Vista creada para el ejercicio practico de Django
def cursoDjango02(request):
    return render(request, "appcursoPython/cursoDjango02.html")


# Vista creada para el listado de libros que se posee
def listado_libros(request):
    return render(request, "appCursoPython/libros.html")


#Vista de la pagina principal de videos complementarios
def videosComplementarios(request):
    return render(request, "appCursoPython/videosComplementarios.html")


# Vista creada para el tutorial de Operadores
def operadores(request):
    return render(request, "appcursoPython/operadores.html")
