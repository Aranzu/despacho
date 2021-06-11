from django.db import models

# Create your models here.
class OrdenRetiro(models.Model):   
    rut = models.CharField(max_length=100, primary_key=True)
    nombre_cl = models.CharField(max_length=100)
    nombre_pro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    horario_ret = models.TimeField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.rut