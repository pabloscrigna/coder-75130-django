from django.http import HttpResponse


def vista_inicial(request):

    return HttpResponse("<h1>Bienvenidos al curso de python</h1>")
