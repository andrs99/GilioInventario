# Generated by Django 2.2.3 on 2021-11-18 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_auto_20211118_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areas',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
