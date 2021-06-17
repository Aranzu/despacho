from django.db import models

# Create your models here.
class OrdenRetiro(models.Model):
    num_solicitud = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100)
    nombre_cl = models.CharField(max_length=100)
    nombre_pro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.rut