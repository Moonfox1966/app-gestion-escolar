from django.db import models
from profesores.models import Profesor
from alumnos.models import Alumno

class Curso(models.Model):
    # # (Alumno) Modelo Curso según Parte IV (1)
    nombre = models.CharField(max_length=120)

    # # (Alumno) un curso lo dicta 1 profesor
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT, related_name="cursos")

    # # (Alumno) un curso tiene muchos alumnos y un alumno puede estar en muchos cursos
    alumnos = models.ManyToManyField(Alumno, related_name="cursos", blank=True)

    def __str__(self):
        return f"{self.nombre}"