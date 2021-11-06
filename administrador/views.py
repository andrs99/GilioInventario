from django.shortcuts import render, redirect
import datetime
# from superSu.models import prueba
from django.http import JsonResponse
from login.models import Usuarios


    

def get_data_user(usr):
    try:
        user = Usuarios.objects.get(email__exact=usr)
        return {"nombre":user.nombre,"apellido":user.apellido, "cargo":user.cargo,"img":user.img, "email": user.email}
    except:
        return 1

def Validar_session(request):
    try:
        if request.session["sesion"]==True and request.session["cargo"]=="administrador":
            return 0
        else:
            return 1
    except:
        return 1

# def AdministradorHome(request):
#     if(Validar_session(request)):
#         return redirect("/login_validar/")
#     datos= get_data_user(request.session["email"])
#     plantilla='administrador/base.html'
#     return render(request,plantilla,datos)


def AdministradorHome(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    plantilla='administrador/home.html'
    return render(request,plantilla,datos)

def AdministradorInventario(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    plantilla='administrador/inventario.html'
    return render(request,plantilla,datos)
