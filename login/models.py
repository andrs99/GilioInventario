from django.db import models
# from django.contrib.auth.models import User

class Usuarios(models.Model):

    TIPO_USUARIOS = (
        ('superusuario', 'Super Usuario'),
        ('administrador', 'Administrador'),
    )

    STATUS = (
        (True, 'Administrador Activo'),
        (False, 'Administrador Inactivo'),
    )

    nombre=models.CharField(max_length=50,null=False, verbose_name="Nombre")
    apellido=models.CharField(max_length=50,null=False, verbose_name="Apellido")
    cargo=models.CharField(max_length=20,choices=TIPO_USUARIOS,null=False, verbose_name="Cargo")
    status=models.BooleanField(choices=STATUS, null=False,verbose_name="Estado")
    fecha_alta=models.DateField(null=False, verbose_name="Fecha de registro")
    fecha_baja=models.DateField(null=True, verbose_name="Fecha de baja")
    fecha_modificacion=models.DateField(null=True, verbose_name="Fecha del ultimo cambio")
    img=models.CharField(max_length=30,null=True, default='img_usuarios/all.jpg', verbose_name="Imagen")
    password=models.CharField(max_length=128,null=False, verbose_name="Contraseña")
    email=models.CharField(max_length=50,null=False, verbose_name="Email")
    # autenticacion=models.ForeignKey(User,null=True, on_delete=models.PROTECT, verbose_name="Licencias")

    def nombre_completo(self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombre_completo



