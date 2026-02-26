#!/usr/bin/env python
import os
import sys

def main():
    # (Alumno) Django usa esta variable para saber qué settings cargar
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App_Gestion_Escolar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Activaste el venv e instalaste Django?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()