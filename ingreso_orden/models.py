from django.db import models

# Create your models here.
class OrdenRetiro(models.Model):
    num_solicitud = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    nombre_cl = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    num_telf = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    nombre_pro = models.CharField(max_length=500)
    direccion = models.CharField(max_length=100)
    estado_orden = models.CharField(max_length=100, default='Pendiente')

    def __str__(self):
        return self.rut