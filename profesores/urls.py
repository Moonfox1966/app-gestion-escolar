from django.urls import path
from .views import lista_profesores, profesor_form_view, resultado_profesor_view

app_name = "profesores"

urlpatterns = [
    path('', lista_profesores, name='lista_profesores'),

    path('ingresar/', profesor_form_view, name='ingresar_profesor'),
    path('resultado/', resultado_profesor_view, name='resultado_profesor'),
]