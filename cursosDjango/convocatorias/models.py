from distutils.command.upload import upload
from operator import mod
from tabnanny import verbose
from django.db import models

class Cursos(models.Model):
    nombreCurso = models.TextField(max_length=50)
    nombreProfesor = models.TextField(max_length=50)
    totalLecciones = models.TextField(max_length=10)
    totalHoras = models.TextField(max_length=15)
    clasificacionCurso = models.TextField(max_length=20)
    fechaPublicacion = models.DateField()
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"
    ordering = ["-created"]

def __str__(self):
    return self.nombre

    
    
