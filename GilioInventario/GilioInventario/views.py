from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime
from django.template.loader import get_template

class persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido
def login(request):

    fecha_agno = datetime.datetime.now().year

    doc_externo=get_template('login/login.html')

    datos_persona=persona("Luis Andres","Rodriguez Campos")

    cursos=["Django","Larabel","React Js","Boostrap","Jquery","C#"]

    datos={"agno":fecha_agno,"datos_persona":datos_persona, "cursos":cursos,"cantidad_cursos":len(cursos)}

    documento = doc_externo.render(datos)

    return HttpResponse(documento)

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