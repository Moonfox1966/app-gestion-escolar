from django.urls import path
from .views import lista_cursos

app_name = "cursos"

urlpatterns = [
    path('', lista_cursos, name='lista_cursos'),
]