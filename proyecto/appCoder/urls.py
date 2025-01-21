from django.urls import path

from .views import (
    cursos, 
    inicio, 
    curso_formulario,
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
    EstudianteListView,
    EstudianteDetailView,
    EstudianteCreateView,
    EstudianteDeleteView,
)

urlpatterns = [
    path("cursos/", cursos, name="cursos"),
    path("inicio/", inicio, name="inicio"),
    path("curso-nuevo", curso_formulario, name="curso_formulario"),
    path("estudiante-nuevo", crear_estudiante, name="crear_estudiante"),
    path("estudiante-listar", listar_estudiantes, name="listar_estudiantes"),
    path("estudiante-buscar/<int:pk>", buscar_estudiante, name="buscar_estudiante"),
    path("estudiante-actualizar/<int:pk>", actualizar_estudiante, name="actualizar_estudiante"),
    path("estudiante-eliminar/<int:pk>", eliminar_estudiante, name="eliminar_estudiante"),
    path("lista-estudiantes", EstudianteListView.as_view(), name="estudiantes_listar" ),
    path("estudiante/<int:pk>", EstudianteDetailView.as_view(), name="estudiante_detail"),
    path("estudiante/nuevo/", EstudianteCreateView.as_view(), name="estudiante_nuevo" ),
    path("estudiante/eliminar/<int:pk>", EstudianteDeleteView.as_view(), name="estudiante_eliminar" ),
]