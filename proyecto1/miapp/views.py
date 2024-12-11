from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"nombre" : "juan Sorin"}
    return render(request, "index.html", context)
