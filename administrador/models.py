from django.db import models
from django.contrib.auth.models import User

from login.models import Usuarios

class Areas(models.Model):
    nombre=models.CharField(max_length=50,null=False, verbose_name="Nombre")
    administrador=models.ForeignKey(Usuarios,null=False, on_delete=models.PROTECT, verbose_name="Administrador")
    img = models.ImageField(upload_to = 'areas/%Y/%m/%d/', null=True, verbose_name="Img")
    fecha_alta=models.DateField(null=False, verbose_name="Fecha de registro")
    fecha_baja=models.DateField(null=True, verbose_name="Fecha de baja")
    fecha_modificacion=models.DateField(null=True, verbose_name="Fecha del ultimo cambio")

    # def nombre_completo(self):
    #     return "{} {}".format(self.nombre,self.administrador)

    # def __str__(self):
    #     return self.nombre_completo()

    def __str__(self):
        return self.nombre

