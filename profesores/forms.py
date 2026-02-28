from django import forms

class ProfesorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    materia = forms.CharField(label="Materia", max_length=100)

    ESTADOS = [
        ("Activo", "Activo"),
        ("Inactivo", "Inactivo"),
    ]
    estado = forms.ChoiceField(label="Estado", choices=ESTADOS)