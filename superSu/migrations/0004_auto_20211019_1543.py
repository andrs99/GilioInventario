# Generated by Django 2.2.3 on 2021-10-19 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('superSu', '0003_usuarios_id_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='autenticacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Licencias'),
        ),
    ]
