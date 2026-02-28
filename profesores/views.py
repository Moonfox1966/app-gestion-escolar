from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import ProfesorForm

@never_cache
@login_required
def lista_profesores(request):
    profesores = [
        {"nombre": "Dra. Elena Rodríguez", "materia": "Matemáticas Avanzadas", "estado": "Activo"},
        {"nombre": "Prof. Carlos Méndez", "materia": "Historia Universal", "estado": "Activo"},
        {"nombre": "Lic. Sofía Valenzuela", "materia": "Literatura y Lengua", "estado": "Activo"},
        {"nombre": "Dr. Ricardo Alarcón", "materia": "Física y Química", "estado": "Activo"},
    ]

    ultimo = request.session.get("ultimo_profesor")
    if ultimo:
        profesores.insert(0, ultimo)

    return render(request, "profesores/lista_profesores.html", {"profesores": profesores})

@never_cache
@login_required
def profesor_form_view(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            request.session["ultimo_profesor"] = form.cleaned_data
            return redirect("profesores:resultado_profesor")
    else:
        form = ProfesorForm()

    return render(request, "profesores/profesor_form.html", {"form": form})

@never_cache
@login_required
def resultado_profesor_view(request):
    profesor = request.session.get("ultimo_profesor")
    return render(request, "profesores/profesor_resultado.html", {"profesor": profesor})