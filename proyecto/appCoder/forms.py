from django import forms

from .models import Estudiante


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()

    def save(self, commit=True):
        estudiante = Estudiante(
            nombre=self.cleaned_data["nombre"],
            apellido=self.cleaned_data["apellido"],
            email=self.cleaned_data["email"]
        )

        if commit:
            estudiante.save()
        
        return estudiante