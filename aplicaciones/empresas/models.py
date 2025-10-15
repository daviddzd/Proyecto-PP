from django.db import models
from django.contrib.auth.models import User
#from django.utils import datetim

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Vacante(models.Model):
    puesto = models.CharField(max_length=200, null=False, blank=False)
    descripcion_vacante = models.CharField(max_length=300)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    salario = models.IntegerField()
    prestaciones = models.CharField(max_length=400)
    requisitos = models.CharField(max_length=400)
    activa = models.BooleanField(default=True)
    postulaciones = models.IntegerField(default=0)


    def __str__(self):
        return self.empresa.nombre + ' : ' +  self.puesto 
