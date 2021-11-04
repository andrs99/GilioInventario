from django.shortcuts import render, redirect
import datetime
from superSu.models import prueba
from django.http import JsonResponse


def Validar_session(request):
    try:
        if request.session["sesion"]==True and request.session["cargo"]=="administrador":
            return 0
        else:
            return 1
    except:
        return 1

def AdministradorHome(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")


    
    nombre = request.session["nombre"]
    apellido = request.session["apellido"]
    cargo = request.session["cargo"].capitalize()
    img = request.session["img"]
    email = request.session["email"]

    datos={"nombre":nombre,"apellido":apellido, "cargo":cargo,"img":img, "email": email}
    plantilla='administrador/home.html'
    return render(request,plantilla,datos)
