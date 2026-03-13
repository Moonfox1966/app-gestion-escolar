from django.urls import path
from .views import (
    lista_cursos,
    curso_form_view,
    resultado_curso_view,
    detalle_curso_view,
    editar_curso_view,
    eliminar_curso_view,
)

app_name = "cursos"

urlpatterns = [
    path("", lista_cursos, name="lista_cursos"),
    path("ingresar/", curso_form_view, name="ingresar_curso"),
    path("resultado/<int:pk>/", resultado_curso_view, name="resultado_curso"),

    path("<int:pk>/detalle/", detalle_curso_view, name="detalle_curso"),
    path("<int:pk>/editar/", editar_curso_view, name="editar_curso"),
    path("<int:pk>/eliminar/", eliminar_curso_view, name="eliminar_curso"),
]