from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views  # login/logout

def inicio(request):
    return render(request, "inicio.html")

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth (vistas predefinidas)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    # Home del sitio
    path('', inicio, name='inicio'),

    # Apps
    path('alumnos/', include('alumnos.urls')),
    path('profesores/', include('profesores.urls')),
    path('cursos/', include('cursos.urls')),
]