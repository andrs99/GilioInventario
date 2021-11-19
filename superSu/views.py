from django.db.models import query
from django.shortcuts import render, redirect
from superSu.models import prueba
from login.models import Usuarios
import datetime

from django.http import JsonResponse

from werkzeug.security import generate_password_hash, check_password_hash


def Validar_session(request):
    try:
        if request.session["sesion"]==True and request.session["cargo"]=="superusuario":
            return 0
        else:
            return 1
    except:
        return 1




def prueba_get(request):

    plantilla='login/form.html'
    datos={"dato":"huevos"}
    print(datos)

    return render(request,plantilla,datos)

def subir(request):
    # ----- CONSULTAS -----
    nombre=request.GET["nombre"]
    try:
        user = prueba.objects.get(nombre=nombre)
        nombre= user.nombre
        apellido=user.apellido
        
        data = {
            'nombre': nombre,
            'apellido': apellido,
            'return': 1
        }
    except:
        data = {
            'resturn': 'no encontrado',
            'return': 0
        }

    return JsonResponse(data)

    

    # ----- ALTA ------
    # nombre=request.POST["nombre"]
    # apellido=request.POST["apellido"]
    # alta=prueba.objects.create(nombre=nombre, apellido=apellido)  
    # alta.save()



    # ----- BAJA -----
    # busqueda=request.POST["buscar"]
    # prueba.objects.filter(id = busqueda).delete()

    # ----- CAMBIO -----
    # busqueda=request.POST["buscar"]
    # cambio=request.POST["nuevo"]
    # acualizar=prueba.objects.get(id=busqueda)
    # acualizar.apellido=cambio
    # acualizar.save()

    # plantilla='login/form.html'

    # return render(request,plantilla)

def busqueda(request):
    plantilla='administrador/busqueda.html'
    return render(request,plantilla)

def busqueda_ajax(request):
    # busqueda=request.GET["busqueda"]
    # print(busqueda)
    # try:
    #     user = prueba.objects.get(nombre=busqueda)
    #     nombre= user.nombre
    #     apellido=user.apellido
        
    #     data = {
    #         'nombre': nombre,
    #         'apellido': apellido,
    #         'return': 1
    #     }
    # except:
    #     data = {
    #         'mensaje': 'no encontrado',
    #         'return': 0
    #     }
    # return JsonResponse(data)

    busqueda=request.GET["busqueda"]
    resultado = prueba.objects.filter(apellido=busqueda)

    if(resultado):
        data = []
        info = {
                'mensaje': "resultados",
                'return': 1
            }
        data.append(info)
        for perfil in resultado:
            info = {
                'nombre': perfil.nombre,
                'apellido': perfil.apellido
            }
            data.append(info)
        return JsonResponse(data, safe=False)
    else:
        data = {
            'mensaje': 'Sin resultados',
            'return': 0
        }
        return JsonResponse(data, safe=False)

def altas(request):
    plantilla='administrador/altas.html'
    return render(request,plantilla)

def altas_ajax(request):
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    alta=prueba.objects.create(nombre=nombre, apellido=apellido)  
    alta.save()

    plantilla='administrador/altas.html'
    return render(request,plantilla)

def Cambios(request):
    plantilla='administrador/cambios.html'
    return render(request,plantilla)

def Cambios_ajax(request):
    busqueda=request.POST["buscar"]
    nuevo_nombre=request.POST["nuevo_nombre"]
    nuevo_apellido=request.POST["nuevo_apellido"]

    acualizar=prueba.objects.get(id=busqueda)
    acualizar.nombre=nuevo_nombre
    acualizar.apellido=nuevo_apellido
    acualizar.save()
    plantilla='administrador/cambios.html'
    return render(request,plantilla)

def Eliminar(request):
    plantilla='administrador/eliminar.html'
    return render(request,plantilla)

def Eliminar_ajax(request):
    busqueda=request.POST["buscar"]
    prueba.objects.filter(id = busqueda).delete()
    plantilla='administrador/eliminar.html'
    return render(request,plantilla)

def Nuevo_usuario(request):



    # ----- ALTA ------
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    cargo=request.POST["cargo"]
    status=True
    fecha_alta=datetime.datetime.today()
    

    email=request.POST["email"]
    password=request.POST["password"]
    password=generate_password_hash(password)



    

    # print(password)
    # print(password_cifrado)
    # print(check_password_hash(password_cifrado,"111"))

    # print(nombre)
    # print(apellido)
    # print(cargo)
    # print(status)
    # print(fecha_alta)
    # print(email)
    # print(password)


    query=Usuarios.objects.create(
        nombre=nombre, 
        apellido=apellido, 
        cargo=cargo, 
        status=status, 
        fecha_alta=fecha_alta, 
        email=email,
        password=password
    )  

    query.save()

    # print("ok")
    # Usuarios.objects.filter(id = 1).delete()
    data = {
        'resturn': 'no encontrado',
        'return': 0
    }
    return JsonResponse(data)

def SuperSuHome(request):
    # if(Validar_session(request)):
    #     return redirect("/login_validar/")
    plantilla='supersu/home.html'
    return render(request,plantilla)