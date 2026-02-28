from django.urls import path
from .views import lista_cursos, curso_form_view, resultado_curso_view

app_name = "cursos"

urlpatterns = [
    path('', lista_cursos, name='lista_cursos'),

    path('ingresar/', curso_form_view, name='ingresar_curso'),
    path('resultado/', resultado_curso_view, name='resultado_curso'),
]