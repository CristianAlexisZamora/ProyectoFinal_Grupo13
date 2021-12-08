from django.shortcuts import render, HttpResponse
from appCursoPython.models import nota
from main.user.models import User

# Create your views here.

# Vista creada para la pagina de inicio (modificar al que le corresponsa solo se ha creado para que no lance error de link)
def home(request):
    return HttpResponse("Inicio")

#Vista de la pagina principal de academia
def academiaCurso(request):
    if request.user.is_authenticated and request.user.premium:
        return render(request, "main/academiaCurso.html", {"premium":True})
    else:
        return render(request, "main/academiaCurso.html", {"premium":False})
#Vista de mi cuenta
def cuenta(request):

    iduser= User.objects.get(id=request.user.id)
    notasUser= nota.objects.filter(id_usuario = iduser)
    modulo1=0
    modulo2=0
    modulo3=0
    modulo4=0

    for registro in notasUser:
        if (registro.nota_practica > 0 and registro.nota_practica < 5):
            modulo1 += registro.nota_practica
        elif(registro.nota_practica > 4 and registro.nota_practica < 8):
            modulo2 += registro.nota_practica
        elif(registro.nota_practica > 7 and registro.nota_practica < 14):
            modulo3 += registro.nota_practica
        else:
            modulo4 += registro.nota_practica

    modulo1/= 4
    modulo2/= 3
    modulo3/= 6
    modulo4/= 6

    contexto = { 
    "Nombre": request.user.first_name,
    "Apellido": request.user.last_name,
    "Edad": request.user.edad,
    "Sexo": request.user.sexo,
    "Usuario":request.user.username,
    "Email":request.user.email,
    "Modulo1":modulo1,
    "Modulo2":modulo2,
    "Modulo3":modulo3,
    "Modulo4":modulo4,
    }

    return render(request, "main/cuenta.html",contexto)


#Vista de acerca de nosotros
def nosotros(request): 
    return render(request, "main/nosotros.html")

#Premium
def activarPremium(request):
    if request.user.is_authenticated:
        User.objects.get(id = request.user.id).update(premium = True)
    