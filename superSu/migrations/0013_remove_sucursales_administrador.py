# Generated by Django 2.2.3 on 2021-10-25 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superSu', '0012_auto_20211025_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursales',
            name='administrador',
        ),
    ]
