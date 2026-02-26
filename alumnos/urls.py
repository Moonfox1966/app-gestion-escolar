from django.urls import path
from .views import lista_alumnos

app_name = "alumnos"

urlpatterns = [
    path('', lista_alumnos, name='lista_alumnos'),
]