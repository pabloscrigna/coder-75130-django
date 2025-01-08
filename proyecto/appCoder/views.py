from django.shortcuts import render, redirect

# Create your views here.

from .models import Curso
from .forms import CursoFormulario

def inicio(request):

    print(f"metodo: {request.method}")

    return render(request, 'inicio.html')

def cursos(request):

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}
    return render(request, 'cursos.html', contexto)

def curso_formulario(request):
    print(f"metodo: {request.method}")
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        print(f"nombre: {form['nombre'].value()}")
        print(f"camada: {form['camada'].value()}")
        if form.is_valid():
            print("El formulario es valido")
            print(f"nombre: {form.cleaned_data['nombre']}")
            print(f"camada: {form.cleaned_data['camada']}")
            curso = Curso(nombre=form.cleaned_data['nombre'], camada=form.cleaned_data['camada'])
            curso.save()
            # return render(request, 'inicio.html')
            return redirect('inicio')

    form = CursoFormulario()
    return render(request, 'curso_formulario.html', {'form': form})
