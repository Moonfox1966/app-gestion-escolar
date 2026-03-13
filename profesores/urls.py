from django.urls import path
from .views import (
    lista_profesores,
    profesor_form_view,
    resultado_profesor_view,
    detalle_profesor_view,
    editar_profesor_view,
    eliminar_profesor_view,
)

app_name = "profesores"

urlpatterns = [
    path("", lista_profesores, name="lista_profesores"),
    path("ingresar/", profesor_form_view, name="ingresar_profesor"),
    path("resultado/<int:pk>/", resultado_profesor_view, name="resultado_profesor"),

    path("<int:pk>/detalle/", detalle_profesor_view, name="detalle_profesor"),
    path("<int:pk>/editar/", editar_profesor_view, name="editar_profesor"),
    path("<int:pk>/eliminar/", eliminar_profesor_view, name="eliminar_profesor"),
]