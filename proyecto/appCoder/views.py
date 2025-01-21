from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import EstudianteForm
from .models import Estudiante

# Create your views here.

from .models import Curso
from .forms import CursoFormulario


def inicio(request):

    print(f"metodo: {request.method}")

    return render(request, "inicio.html")


def cursos(request):

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}
    return render(request, "cursos.html", contexto)


def curso_formulario(request):
    print(f"metodo: {request.method}")
    if request.method == "POST":
        form = CursoFormulario(request.POST)
        print(f"nombre: {form['nombre'].value()}")
        print(f"camada: {form['camada'].value()}")
        if form.is_valid():
            print("El formulario es valido")
            print(f"nombre: {form.cleaned_data['nombre']}")
            print(f"camada: {form.cleaned_data['camada']}")
            curso = Curso(
                nombre=form.cleaned_data["nombre"], camada=form.cleaned_data["camada"]
            )
            curso.save()
            # return render(request, 'inicio.html')
            return redirect("inicio")

    form = CursoFormulario()
    return render(request, "curso_formulario.html", {"form": form})


def crear_estudiante(request):

    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")

    form = EstudianteForm()
    return render(request, "crear_estudiante.html", {"form": form})


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    contexto = {"estudiantes": estudiantes}

    return render(request, "lista_estudiantes.html", contexto)


def buscar_estudiante(request, pk):
    print(pk)
    estudiante = Estudiante.objects.get(pk=pk)

    contexto = {"estudiante": estudiante}

    return render(request, "lista_estudiante.html", contexto)


def actualizar_estudiante(request, pk):
    estudiante = Estudiante.objects.get(pk=pk)

    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_estudiantes")

    form = EstudianteForm(
        initial={
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "email": estudiante.email,
        }
    )
    return render(
        request,
        "editar_estudiante.html",
        {"form": form, "estudiante_id": estudiante.pk},
    )


@login_required
def eliminar_estudiante(request, pk):
    estudiante = Estudiante.objects.get(pk=pk)

    estudiante.delete()

    return redirect("listar_estudiantes")


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy


class EstudianteListView(ListView):
    model = Estudiante
    template_name = "lista_estudiantes.html"
    context_object_name = "estudiantes"


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "lista_estudiante.html"
    context_object_name = "estudiante"


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    template_name = "crear_estudiante.html"
    success_url = reverse_lazy("lista_estudiantes")


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "confirmacion_delete.html"
    success_url = reverse_lazy("listar_estudiantes")
