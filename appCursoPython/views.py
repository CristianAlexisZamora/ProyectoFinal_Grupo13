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

# Vista creada para el tutorial de Operadores
def operadores(request):
    return render(request, "appcursoPython/operadores.html")