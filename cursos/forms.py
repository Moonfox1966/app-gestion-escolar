from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "profesor", "alumnos"]
        widgets = {
            # # (Alumno) Para seleccionar varios alumnos con Ctrl/Cmd
            "alumnos": forms.SelectMultiple()
        }