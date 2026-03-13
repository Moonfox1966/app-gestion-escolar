from django.contrib import admin
from django.urls import path, include
from .views import inicio_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio_view, name="inicio"),
    path("alumnos/", include("alumnos.urls")),
    path("profesores/", include("profesores.urls")),
    path("cursos/", include("cursos.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]