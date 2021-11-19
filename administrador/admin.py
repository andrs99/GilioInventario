from django.contrib import admin

from login.models import Usuarios
from administrador.models import Areas

admin.site.register(Usuarios)
admin.site.register(Areas)

