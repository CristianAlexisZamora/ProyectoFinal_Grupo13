from django.shortcuts import render, HttpResponse

# Create your views here.

# Vista creada para la pagina de inicio (modificar al que le corresponsa solo se ha creado para que no lance error de link)
def home(request):
    return HttpResponse("Inicio")

#Vista de la pagina principal de academia
def academiaCurso(request):
    return render(request, "main/academiaCurso.html")