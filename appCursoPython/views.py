from django.shortcuts import render

# Create your views here.
# Vista creada para la pagina de POO en python
def pythonPOO(request):

    return render(request, "appCursoPython/pythonPOO.html")

# Vista creada para el curso del framework Django
def frameworkDjango(request):

    return render(request, "appCursoPython/frameworkTeoria.html")

# Vista creada para el ejercicio practico de Django
def ejercicioDjango(request):

    return render(request, "appcursoPython/ejercicioPractico.html")

# Vista creada para el listado de libros que se posee
def listado_libros(request):

    return render(request, "appCursoPython/libros.html")

#Vista de la pagina principal de videos complementarios
def videosComplementarios(request):
    return render(request, "appCursoPython/videosComplementarios.html")