from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

def lista_cursos(request):
    # # (Alumno) traigo profesor en la misma consulta
    cursos = Curso.objects.select_related("profesor").prefetch_related("alumnos").all().order_by("nombre")
    return render(request, "cursos/lista_cursos.html", {"cursos": cursos})

def curso_form_view(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect("cursos:resultado_curso", pk=curso.pk)
    else:
        form = CursoForm()

    return render(request, "cursos/curso_form.html", {"form": form})

def resultado_curso_view(request, pk):
    curso = get_object_or_404(Curso.objects.select_related("profesor").prefetch_related("alumnos"), pk=pk)
    return render(request, "cursos/curso_resultado.html", {"curso": curso})