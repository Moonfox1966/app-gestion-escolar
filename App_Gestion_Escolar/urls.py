from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def inicio(request):
    # (Alumno) portada simple que usa base.html
    return render(request, "inicio.html")

urlpatterns = [
    path('admin/', admin.site.urls),

    # (Alumno) Home del sitio
    path('', inicio, name='inicio'),

    # (Alumno) Apps
    path('alumnos/', include('alumnos.urls')),
    path('profesores/', include('profesores.urls')),
    path('cursos/', include('cursos.urls')),
]