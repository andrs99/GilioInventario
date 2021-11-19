from django.shortcuts import render, redirect
import datetime
# from superSu.models import prueba
from django.http import JsonResponse
from login.models import Usuarios
from administrador.models import Areas
import os


    

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

def AdministradorHome(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    datos['vista'] = "Dashboard"
    plantilla='administrador/home.html'
    return render(request,plantilla,datos)

def AdministradorInventario(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    datos['vista'] = "Inventario"
    plantilla='administrador/inventario.html'
    return render(request,plantilla,datos)

def AdministradorNuevoArticulo(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    datos['vista'] = "Nuevo articulo"


    datos['sucursales']=Areas.objects.filter(administrador_id=request.session["id_usuario"])
 
    
    plantilla='administrador/nuevo-articulo.html'
    return render(request,plantilla,datos)

def AdministradorAreas(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    datos['vista'] = "Areas"
    plantilla='administrador/areas.html'
    return render(request,plantilla,datos)

def AdministradorNuevaArea(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    datos= get_data_user(request.session["email"])
    datos['vista'] = "Nueva area"
    plantilla='administrador/nueva-area.html'
    return render(request,plantilla,datos)

def Guardar_area(request):

    data = {
            'mensaje': 'Usuario o contraseña incorrecta',
            'return': 0
        }

    # img=request.FILES.GET["imgArticulo"]
    id_usuario=request.session["id_usuario"]
    nombre=request.POST["nombre"]
    img=request.FILES['imgArea']
    fecha_alta=datetime.datetime.today()

    query=Areas.objects.create(
        nombre=nombre, 
        img=img, 
        fecha_alta=fecha_alta,
        administrador_id=id_usuario
    )  

    

    return JsonResponse(data)
    

