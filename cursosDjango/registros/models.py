from ensurepip import version
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

class Cursos(models.Model):
    nombreCurso = models.TextField(verbose_name="")
    nombreProfesor = models.TextField()
    categoria = models.TextField()
    duracion = models.TextField()
    fechaPublicacion = models.DateTimeField()

class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"
    ordering = ["-created"]
    #El menos(-created) indica que se ordenará del más nuevo al más viejo

def __str__(self):
    return self.nombre
    #Indica que se mostrará el nombre como valor en la tabla

