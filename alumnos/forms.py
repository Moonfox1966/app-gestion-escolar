from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    # # (Alumno) ModelForm basado en el modelo Alumno
    class Meta:
        model = Alumno
        fields = ["nombre", "apellido", "edad", "correo"]