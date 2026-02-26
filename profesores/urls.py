from django.urls import path
from .views import lista_profesores

app_name = "profesores"

urlpatterns = [
    path('', lista_profesores, name='lista_profesores'),
]