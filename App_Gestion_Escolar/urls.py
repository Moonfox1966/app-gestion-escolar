from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect

def inicio(request):
    return render(request, "inicio.html")

def login_redirect(request):

    return redirect("login")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", login_redirect),
    path("", inicio, name="inicio"),
    path("alumnos/", include("alumnos.urls")),
    path("profesores/", include("profesores.urls")),
    path("cursos/", include("cursos.urls")),
]