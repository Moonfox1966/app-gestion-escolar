from django.urls import path
from .views import (
    lista_alumnos,
    alumno_form_view,
    resultado_alumno_view,
    detalle_alumno_view,
    editar_alumno_view,
    eliminar_alumno_view,
)

app_name = "alumnos"

urlpatterns = [
    path("", lista_alumnos, name="lista_alumnos"),
    path("ingresar/", alumno_form_view, name="ingresar_alumno"),
    path("resultado/<int:pk>/", resultado_alumno_view, name="resultado_alumno"),

    path("<int:pk>/detalle/", detalle_alumno_view, name="detalle_alumno"),
    path("<int:pk>/editar/", editar_alumno_view, name="editar_alumno"),
    path("<int:pk>/eliminar/", eliminar_alumno_view, name="eliminar_alumno"),
]