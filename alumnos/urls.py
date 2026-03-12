from django.urls import path
from .views import lista_alumnos, alumno_form_view, resultado_alumno_view

app_name = "alumnos"

urlpatterns = [
    path("", lista_alumnos, name="lista_alumnos"),
    path("ingresar/", alumno_form_view, name="ingresar_alumno"),
    path("resultado/<int:pk>/", resultado_alumno_view, name="resultado_alumno"),
]