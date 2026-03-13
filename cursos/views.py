from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import CursoForm

@login_required
def lista_cursos(request):
    cursos = (
        Curso.objects
        .select_related("profesor")
        .prefetch_related("alumnos")
        .all()
        .order_by("nombre")
    )
    return render(request, "cursos/lista_cursos.html", {"cursos": cursos})

@login_required
def curso_form_view(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect("cursos:resultado_curso", pk=curso.pk)
    else:
        form = CursoForm()

    return render(
        request,
        "cursos/curso_form.html",
        {
            "form": form,
            "modo": "crear",
        },
    )

@login_required
def resultado_curso_view(request, pk):
    curso = get_object_or_404(
        Curso.objects.select_related("profesor").prefetch_related("alumnos"),
        pk=pk
    )
    return render(request, "cursos/curso_resultado.html", {"curso": curso})

@login_required
def detalle_curso_view(request, pk):
    curso = get_object_or_404(
        Curso.objects.select_related("profesor").prefetch_related("alumnos"),
        pk=pk
    )
    return render(request, "cursos/curso_detalle.html", {"curso": curso})

@login_required
def editar_curso_view(request, pk):
    curso = get_object_or_404(
        Curso.objects.select_related("profesor").prefetch_related("alumnos"),
        pk=pk
    )

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()
            return redirect("cursos:detalle_curso", pk=curso.pk)
    else:
        form = CursoForm(instance=curso)

    return render(
        request,
        "cursos/curso_form.html",
        {
            "form": form,
            "curso": curso,
            "modo": "editar",
        },
    )

@login_required
def eliminar_curso_view(request, pk):
    curso = get_object_or_404(
        Curso.objects.select_related("profesor").prefetch_related("alumnos"),
        pk=pk
    )

    if request.method == "POST":
        curso.delete()
        return redirect("cursos:lista_cursos")

    return render(
        request,
        "cursos/curso_confirm_delete.html",
        {"curso": curso},
    )