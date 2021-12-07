from django.shortcuts import render, HttpResponse
from appCursoPython.models import nota
from main.user.models import User

# Create your views here.

# Vista creada para la pagina de inicio (modificar al que le corresponsa solo se ha creado para que no lance error de link)
def home(request):
    return HttpResponse("Inicio")

#Vista de la pagina principal de academia
def academiaCurso(request):
    return render(request, "main/academiaCurso.html")

#Vista de mi cuenta
def cuenta(request):

    iduser= User.objects.get(id=request.user.id)
    notasUser= nota.objects.filter(id_usuario = iduser)
    modulo1=0
    modulo2=0
    modulo3=0
    modulo4=0

    for registro in notasUser:
        if (registro.id_practica.idpractica > 0 and registro.id_practica.idpractica < 5):
            modulo1 += registro.id_practica.idpractica
        elif(registro.id_practica.idpractica > 4 and registro.id_practica.idpractica < 8):
            modulo2 += registro.id_practica.idpractica
        elif(registro.id_practica.idpractica > 7 and registro.id_practica.idpractica < 14):
            modulo3 += registro.id_practica.idpractica
        else:
            modulo4 += registro.id_practica.idpractica
    #modulo1/= 4
    #modulo2/= 3
    #modulo3/= 6
    #modulo4/= 6

    contexto = { 
    "Nombre": request.user.first_name,
    "Apellido": request.user.last_name,
    "Edad": request.user.edad,
    "Sexo": request.user.sexo,
    "Usuario":request.user.username,
    "Modulo1":modulo1,
    "Modulo2":modulo2,
    "Modulo3":modulo3,
    "Modulo4":modulo4,
    }

    return render(request, "main/cuenta.html",contexto)


#Vista de acerca de nosotros
def nosotros(request): 
    return render(request, "main/nosotros.html")

