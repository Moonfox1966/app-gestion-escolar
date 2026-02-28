from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import AlumnoForm

@never_cache
@login_required
def lista_alumnos(request):
    alumnos = [
        {"nombre": "Alejandro García", "grado": "10º Grado", "seccion": "Sección B", "estado": "Activo"},
        {"nombre": "Sofía Martínez", "grado": "11º Grado", "seccion": "Sección A", "estado": "Activo"},
        {"nombre": "Mateo Rodríguez", "grado": "9º Grado", "seccion": "Sección C", "estado": "Ausente"},
        {"nombre": "Lucía Torres", "grado": "12º Grado", "seccion": "Sección B", "estado": "Activo"},
        {"nombre": "Daniel López", "grado": "10º Grado", "seccion": "Sección A", "estado": "Tarde"},
    ]

    ultimo = request.session.get("ultimo_alumno")
    if ultimo:
        alumnos.insert(0, ultimo)

    return render(request, "alumnos/lista_alumnos.html", {"alumnos": alumnos})

@never_cache
@login_required
def alumno_form_view(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            request.session["ultimo_alumno"] = form.cleaned_data
            return redirect("alumnos:resultado_alumno")
    else:
        form = AlumnoForm()

    return render(request, "alumnos/alumno_form.html", {"form": form})

@never_cache
@login_required
def resultado_alumno_view(request):
    alumno = request.session.get("ultimo_alumno")
    return render(request, "alumnos/alumno_resultado.html", {"alumno": alumno})