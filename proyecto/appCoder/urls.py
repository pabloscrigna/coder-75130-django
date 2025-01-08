from django.urls import path

from .views import cursos, inicio, curso_formulario

urlpatterns = [
    path("cursos/", cursos, name="cursos"),
    path("inicio/", inicio, name="inicio"),
    path("curso-nuevo", curso_formulario, name="curso_formulario"),
]