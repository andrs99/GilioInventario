from django.contrib import admin
from django.urls import path

# from GilioInventario.views import login, administrador
from superSu.views import *
from login.views import *
from administrador.views import *


from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.login, name="login"),
    
    path('', login),
    path('logout/', logout),
    path('login_ajax/', login_ajax),
    path('login_validar/', ValidarUsuario),




    path('super-usuario/', SuperSuHome),
    path('nuevo-usuario/', Nuevo_usuario),






    path('administrador/', AdministradorHome),
    path('administrador/inventario', AdministradorInventario),
    path('administrador/nuevo-articulo', AdministradorNuevoArticulo),

    path('administrador/areas', AdministradorAreas),
    path('administrador/nueva-area', AdministradorNuevaArea),
    path('administrador/guardar-area', Guardar_area),
























    # path('administrador/', administrador),
    path('prueba/', prueba_get),
    path('prueba_up/', subir),




    path('buscar/', busqueda),
    path('buscar_ajax/', busqueda_ajax),

    path('altas/', altas),
    path('altas_ajax/', altas_ajax),


    path('cambios/', Cambios),
    path('cambios_ajax/', Cambios_ajax),

    path('eliminar/', Eliminar),
    path('eliminar_ajax/', Eliminar_ajax),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
