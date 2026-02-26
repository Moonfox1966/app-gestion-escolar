from django.shortcuts import render

def lista_alumnos(request):
    # (Alumno) datos inventados, como pide la guía, para mostrar dinámico
    alumnos = [
        {"nombre": "Alejandro García", "grado": "10º Grado", "seccion": "Sección B", "estado": "Activo"},
        {"nombre": "Sofía Martínez", "grado": "11º Grado", "seccion": "Sección A", "estado": "Activo"},
        {"nombre": "Mateo Rodríguez", "grado": "9º Grado", "seccion": "Sección C", "estado": "Ausente"},
        {"nombre": "Lucía Torres", "grado": "12º Grado", "seccion": "Sección B", "estado": "Activo"},
        {"nombre": "Daniel López", "grado": "10º Grado", "seccion": "Sección A", "estado": "Tarde"},
    ]

    contexto = {"alumnos": alumnos}
    return render(request, "alumnos/lista_alumnos.html", contexto)