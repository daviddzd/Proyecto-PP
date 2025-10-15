from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    cod_post = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=False)
    biogradia = models.TextField(blank=True, null=True)
    
    exp_laboral = models.TextField(blank=True, null=True)
    educacion = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    best_work = models.TextField(blank=True, null=True)
    last_work = models.TextField(blank=True, null=True)
    nivel_experiencia = models.CharField(max_length=50, blank=True, null=True)
    
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre