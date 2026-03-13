from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profesor
from .forms import ProfesorForm

@login_required
def lista_profesores(request):
    profesores = Profesor.objects.all().order_by("apellido", "nombre")
    return render(request, "profesores/lista_profesores.html", {"profesores": profesores})

@login_required
def profesor_form_view(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save()
            return redirect("profesores:resultado_profesor", pk=profesor.pk)
    else:
        form = ProfesorForm()

    return render(
        request,
        "profesores/profesor_form.html",
        {
            "form": form,
            "modo": "crear",
        },
    )

@login_required
def resultado_profesor_view(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, "profesores/profesor_resultado.html", {"profesor": profesor})

@login_required
def detalle_profesor_view(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, "profesores/profesor_detalle.html", {"profesor": profesor})

@login_required
def editar_profesor_view(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)

    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            profesor = form.save()
            return redirect("profesores:detalle_profesor", pk=profesor.pk)
    else:
        form = ProfesorForm(instance=profesor)

    return render(
        request,
        "profesores/profesor_form.html",
        {
            "form": form,
            "profesor": profesor,
            "modo": "editar",
        },
    )

@login_required
def eliminar_profesor_view(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)

    if request.method == "POST":
        profesor.delete()
        return redirect("profesores:lista_profesores")

    return render(
        request,
        "profesores/profesor_confirm_delete.html",
        {"profesor": profesor},
    )