# Generated by Django 2.2.3 on 2021-10-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superSu', '0009_auto_20211020_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='apellido',
        ),
        migrations.AlterField(
            model_name='prueba',
            name='nombre',
            field=models.CharField(default=1, max_length=50, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]