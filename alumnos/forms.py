from django import forms

class AlumnoForm(forms.Form):
    # (Alumno) Campos mínimos para "ingresar alumno"
    nombre = forms.CharField(label="Nombre", max_length=100)
    grado = forms.CharField(label="Grado", max_length=30)
    seccion = forms.CharField(label="Sección", max_length=30)

    ESTADOS = [
        ("Activo", "Activo"),
        ("Ausente", "Ausente"),
        ("Tarde", "Tarde"),
    ]
    estado = forms.ChoiceField(label="Estado", choices=ESTADOS)