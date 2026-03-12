from django.db import models

class Profesor(models.Model):
    # # (Alumno) Modelo Profesor según Parte IV (1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    profesion = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"