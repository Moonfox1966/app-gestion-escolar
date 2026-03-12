from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from .forms import ProfesorForm

def lista_profesores(request):
    profesores = Profesor.objects.all().order_by("apellido", "nombre")
    return render(request, "profesores/lista_profesores.html", {"profesores": profesores})

def profesor_form_view(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save()
            return redirect("profesores:resultado_profesor", pk=profesor.pk)
    else:
        form = ProfesorForm()

    return render(request, "profesores/profesor_form.html", {"form": form})

def resultado_profesor_view(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, "profesores/profesor_resultado.html", {"profesor": profesor})