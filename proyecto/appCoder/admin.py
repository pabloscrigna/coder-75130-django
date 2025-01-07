from django.contrib import admin

# Register your models here.
from .models import Curso, Profesor

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada', 'creado')
    search_fields = ('nombre', 'camada')
    list_filter = ('camada', 'creado')
    ordering = ('creado',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'creado')
    search_fields = ('nombre', 'apellido', 'edad')
    list_filter = ('edad', 'creado')
    ordering = ('creado',)