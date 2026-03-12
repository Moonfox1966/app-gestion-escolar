from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    # # (Alumno) listado real desde BD
    alumnos = Alumno.objects.all().order_by("apellido", "nombre")
    return render(request, "alumnos/lista_alumnos.html", {"alumnos": alumnos})

def alumno_form_view(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()  # # (Alumno) guarda en BD
            return redirect("alumnos:resultado_alumno", pk=alumno.pk)
    else:
        form = AlumnoForm()

    return render(request, "alumnos/alumno_form.html", {"form": form})

def resultado_alumno_view(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, "alumnos/alumno_resultado.html", {"alumno": alumno})