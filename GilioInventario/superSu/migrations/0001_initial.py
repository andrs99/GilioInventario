# Generated by Django 2.2.3 on 2021-10-19 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('cargo', models.CharField(choices=[('superSu', 'Super Usuario'), ('administrador', 'Administrador')], max_length=20, verbose_name='Cargo')),
                ('status', models.BooleanField(choices=[(True, 'Administrador Activo'), (False, 'Administrador Inactivo')], verbose_name='Estado')),
                ('fecha_alta', models.DateField(verbose_name='Fecha de registro')),
                ('fecha_baja', models.DateField(null=True, verbose_name='Fecha de baja')),
                ('fecha_modificacion', models.DateField(null=True, verbose_name='Fecha del ultimo cambio')),
                ('img', models.CharField(default='img_usuarios/all.jpg', max_length=30, null=True, verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la sucursal')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('municipio', models.CharField(max_length=50, verbose_name='Municipio')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('direccion', models.CharField(max_length=50, verbose_name='Ubicacion')),
                ('numero_materias', models.IntegerField(null=True, verbose_name='Cantidad de material')),
                ('img', models.CharField(default='img_sucursales/all.jpg', max_length=30, null=True, verbose_name='Imagen')),
                ('fecha_alta', models.DateField(verbose_name='Fecha de registro')),
                ('fecha_baja', models.DateField(null=True, verbose_name='Fecha de baja')),
                ('fecha_modificacion', models.DateField(null=True, verbose_name='Fecha del ultimo cambio')),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='superSu.Usuarios', verbose_name='Administrador')),
            ],
        ),
    ]
