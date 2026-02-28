from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del curso", max_length=120)
    codigo = forms.CharField(label="Código", max_length=20)
    profesor = forms.CharField(label="Profesor", max_length=120)
    horario = forms.CharField(label="Horario", max_length=120)

    NIVELES = [
        ("Primaria", "Primaria"),
        ("Secundaria", "Secundaria"),
        ("Bachillerato", "Bachillerato"),
    ]
    nivel = forms.ChoiceField(label="Nivel", choices=NIVELES)