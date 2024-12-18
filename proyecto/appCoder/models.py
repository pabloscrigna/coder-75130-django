from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    camada = models.IntegerField()
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre