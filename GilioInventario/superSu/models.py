from django.db import models
from login.models import Usuarios



class Sucursales(models.Model):
    nombre=models.CharField(max_length=30, null=False, verbose_name="Nombre de la sucursal")
    pais=models.CharField(max_length=50, null=False, verbose_name="Pais")
    estado=models.CharField(max_length=50, null=False, verbose_name="Estado")
    municipio=models.CharField(max_length=50, null=False, verbose_name="Municipio")
    localidad=models.CharField(max_length=50, null=False, verbose_name="Localidad")
    direccion=models.CharField(max_length=50, null=False, verbose_name="Ubicacion")
    numero_materias=models.IntegerField(null=True, verbose_name="Cantidad de material")
    img=models.CharField(max_length=30,null=True, default='img_sucursales/all.jpg', verbose_name="Imagen")
    fecha_alta=models.DateField(null=False, verbose_name="Fecha de registro")
    fecha_baja=models.DateField(null=True, verbose_name="Fecha de baja")
    fecha_modificacion=models.DateField(null=True, verbose_name="Fecha del ultimo cambio")
    # administrador = models.ForeignKey(Usuarios,null=False, on_delete=models.PROTECT, verbose_name="Administrador")

    def nombre_sucursal(self):
        return "{} {}".format(self.nombre,self.municipio)

    def __str__(self):
        return self.nombre_sucursal 

class prueba(models.Model):
    nombre=models.CharField(max_length=50,null=False, verbose_name="Nombre")
    apellido=models.CharField(max_length=50,null=True, verbose_name="Apellido")

    def __str__(self):
        return '%s %s'% (self.nombre, self.apellido)
    

    # def nombre_user(self):
    #     return "{} {}".format(self.apellido,self.nombre)

    

    
