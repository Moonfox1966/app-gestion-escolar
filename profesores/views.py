from django.shortcuts import render

def lista_profesores(request):
    profesores = [
        {"nombre": "Dra. Elena Rodríguez", "materia": "Matemáticas Avanzadas", "estado": "Activo"},
        {"nombre": "Prof. Carlos Méndez", "materia": "Historia Universal", "estado": "Activo"},
        {"nombre": "Lic. Sofía Valenzuela", "materia": "Literatura y Lengua", "estado": "Activo"},
        {"nombre": "Dr. Ricardo Alarcón", "materia": "Física y Química", "estado": "Activo"},
    ]

    contexto = {"profesores": profesores}
    return render(request, "profesores/lista_profesores.html", contexto)