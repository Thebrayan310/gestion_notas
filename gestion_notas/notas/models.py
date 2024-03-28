from django.db import models

class Tarea(models.Model):
    equipo = models.CharField(max_length=100)
    fecha_mantenimiento = models.DateField()
    procedimiento = models.TextField()




