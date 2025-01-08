from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'AC', 'Activo'
        INACTIVO = 'IN', 'Inactivo'
        BORRADOR = 'BO', 'Borrador'

    nombre = models.CharField(max_length=20, unique=True)
    camada = models.IntegerField()
    creado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.BORRADOR)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    creado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre