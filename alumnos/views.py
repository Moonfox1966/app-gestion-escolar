from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm

@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all().order_by("apellido", "nombre")
    return render(request, "alumnos/lista_alumnos.html", {"alumnos": alumnos})

@login_required
def alumno_form_view(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            return redirect("alumnos:resultado_alumno", pk=alumno.pk)
    else:
        form = AlumnoForm()

    return render(request, "alumnos/alumno_form.html", {"form": form, "modo": "crear"})

@login_required
def resultado_alumno_view(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, "alumnos/alumno_resultado.html", {"alumno": alumno})

@login_required
def detalle_alumno_view(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, "alumnos/alumno_detalle.html", {"alumno": alumno})

@login_required
def editar_alumno_view(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)

    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save()
            return redirect("alumnos:detalle_alumno", pk=alumno.pk)
    else:
        form = AlumnoForm(instance=alumno)

    return render(
        request,
        "alumnos/alumno_form.html",
        {
            "form": form,
            "alumno": alumno,
            "modo": "editar",
        },
    )

@login_required
def eliminar_alumno_view(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)

    if request.method == "POST":
        alumno.delete()
        return redirect("alumnos:lista_alumnos")

    return render(
        request,
        "alumnos/alumno_confirm_delete.html",
        {"alumno": alumno},
    )