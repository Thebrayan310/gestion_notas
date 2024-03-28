# Generated by Django 5.0.3 on 2024-03-27 05:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='nombre',
        ),
        migrations.AddField(
            model_name='tarea',
            name='equipo',
            field=models.CharField(default='valor_por_defecto', max_length=200),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_mantenimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tarea',
            name='procedimiento',
            field=models.TextField(default=''),
        ),
    ]