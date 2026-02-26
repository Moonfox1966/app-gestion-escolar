from django.shortcuts import render

def lista_cursos(request):
    cursos = [
        {
            "nombre": "Matemáticas Avanzadas",
            "codigo": "MAT-402",
            "profesor": "Prof. Ricardo Méndez",
            "horario": "Lun, Mie - 08:00 AM",
            "nivel": "Secundaria",
            "icono": "calculate",
            "gradiente": "from-blue-600 to-primary",
        },
        {
            "nombre": "Historia Universal",
            "codigo": "HIS-201",
            "profesor": "Prof. Elena Santos",
            "horario": "Mar, Jue - 10:30 AM",
            "nivel": "Bachillerato",
            "icono": "history_edu",
            "gradiente": "from-amber-500 to-orange-600",
        },
        {
            "nombre": "Ciencias Naturales",
            "codigo": "CIE-105",
            "profesor": "Prof. Carlos Ruiz",
            "horario": "Vie - 09:00 AM",
            "nivel": "Primaria",
            "icono": "biotech",
            "gradiente": "from-emerald-500 to-teal-700",
        },
        {
            "nombre": "Literatura Hispana",
            "codigo": "LIT-330",
            "profesor": "Dra. Marta Villa",
            "horario": "Mie, Jue - 12:00 PM",
            "nivel": "Secundaria",
            "icono": "auto_stories",
            "gradiente": "from-purple-500 to-indigo-700",
        },
        {
            "nombre": "Física Mecánica",
            "codigo": "FIS-450",
            "profesor": "Ing. Sergio Lara",
            "horario": "Lun, Vie - 10:30 AM",
            "nivel": "Bachillerato",
            "icono": "rocket_launch",
            "gradiente": "from-red-500 to-rose-700",
        },
        {
            "nombre": "Artes Plásticas",
            "codigo": "ART-101",
            "profesor": "Prof. Sofía Luna",
            "horario": "Mar - 02:00 PM",
            "nivel": "Primaria",
            "icono": "palette",
            "gradiente": "from-pink-500 to-fuchsia-600",
        },
    ]

    contexto = {"cursos": cursos}
    return render(request, "cursos/lista_cursos.html", contexto)