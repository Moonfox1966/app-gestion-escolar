from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import CursoForm

@never_cache
@login_required
def lista_cursos(request):
    cursos = [
        {"nombre": "Matemáticas Avanzadas", "codigo": "MAT-402", "profesor": "Prof. Ricardo Méndez", "horario": "Lun, Mie - 08:00 AM", "nivel": "Secundaria"},
        {"nombre": "Historia Universal", "codigo": "HIS-201", "profesor": "Prof. Elena Santos", "horario": "Mar, Jue - 10:30 AM", "nivel": "Bachillerato"},
        {"nombre": "Ciencias Naturales", "codigo": "CIE-105", "profesor": "Prof. Carlos Ruiz", "horario": "Vie - 09:00 AM", "nivel": "Primaria"},
    ]

    ultimo = request.session.get("ultimo_curso")
    if ultimo:
        cursos.insert(0, ultimo)

    return render(request, "cursos/lista_cursos.html", {"cursos": cursos})

@never_cache
@login_required
def curso_form_view(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            request.session["ultimo_curso"] = form.cleaned_data
            return redirect("cursos:resultado_curso")
    else:
        form = CursoForm()

    return render(request, "cursos/curso_form.html", {"form": form})

@never_cache
@login_required
def resultado_curso_view(request):
    curso = request.session.get("ultimo_curso")
    return render(request, "cursos/curso_resultado.html", {"curso": curso})