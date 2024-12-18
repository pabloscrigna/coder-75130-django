from django.shortcuts import render

# Create your views here.

from .models import Curso


def cursos(request):

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}
    return render(request, 'cursos.html', contexto)
