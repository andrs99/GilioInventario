from django.shortcuts import render, redirect
import datetime
from superSu.models import prueba
from login.models import Usuarios
from django.http import JsonResponse
from werkzeug.security import generate_password_hash, check_password_hash

def ValidarUsuario(request):
    try:
        if request.session["sesion"]==True:
            if(request.session["cargo"]=="administrador"):
                return redirect("/administrador/")
            elif(request.session["cargo"]=="superusuario"):
                return redirect("/super-usuario/")
    except:
        pass
    return redirect("http://127.0.0.1:8000/")


def Validar_session(request):
    try:
        if request.session["sesion"]==True:
            return 1
    except:
        return 0

def login(request):
    if(Validar_session(request)):
        return redirect("/login_validar/")
    fecha_agno = datetime.datetime.now().year
    plantilla='login/login.html'
    datos={"agno":fecha_agno}
    return render(request,plantilla,datos)

def login_ajax(request):
    data = {}
    usuario=str(request.GET["usuario"])
    usuario.rstrip()
    password=request.GET["password"]   

    try:
        user = Usuarios.objects.get(email__exact=usuario)
        password_db=user.password
        if(check_password_hash(password_db,password)):
            request.session["id_usuario"] = user.id
            request.session["sesion"] = True
            request.session["cargo"] = user.cargo
            request.session["nombre"] = user.nombre
            request.session["apellido"] = user.apellido
            request.session["img"] = user.img
            request.session["email"] = user.email

            data = {
                'mensaje': 'Ususario valido',
                'return': 1
            }
        else:
            data = {
                'mensaje': 'Usuario o contraseña incorrecta',
                'return': 0
            }
    except:
        data = {
            'mensaje': 'Usuario o contraseña incorrecta',
            'return': 0
        }
    return JsonResponse(data)

def logout(request):
    try:
        del request.session['sesion']
        del request.session["cargo"]
        del request.session["email"]
    except:
        pass
    return redirect("http://127.0.0.1:8000/")

