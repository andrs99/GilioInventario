# Generated by Django 2.2.3 on 2021-10-26 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='autenticacion',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='Contraseña'),
            preserve_default=False,
        ),
    ]