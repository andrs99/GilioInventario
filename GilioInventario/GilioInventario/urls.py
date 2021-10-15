from django.contrib import admin
from django.urls import path

from GilioInventario.views import login, logout, fecha, calculaEdad


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login),
    path('logout/', logout),
    path('fecha/', fecha),

    path('edad/<int:edad>/<int:agno>', calculaEdad),
]
