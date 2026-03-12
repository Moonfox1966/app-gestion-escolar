from django.db import models

class Alumno(models.Model):
    # # (Alumno) Modelo Alumno según Parte IV (1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        # # (Alumno) Esto se ve en el admin
        return f"{self.nombre} {self.apellido} ({self.correo})"