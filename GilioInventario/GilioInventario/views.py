from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime


def login(request):
    return HttpResponse("Aqui va el login")

def logout(reques):
    return HttpResponse("Salir de Gilio")

def fecha(request):
    fecha=datetime.datetime.now().year

    documento="""
        <html>
            <body>
                <h1>La fecha actual es %s
            </body>
        </html>
    """%fecha
    return HttpResponse(documento)


def calculaEdad(request, edad, agno):



    periodo=agno-2021

    edadFutura=edad+periodo

    documento="""
        <html>
            <body>
                <label>En el año %s tendras: </label>
                <br>
                <label>%s años</label>
            </body>
        </html>
    """%(agno,edadFutura)

    return HttpResponse(documento)