from urllib import request
from django.shortcuts import render
from .models import Cursos

def convocatorias(request):
    cursos = Cursos.objects.all()
    return render(request, "convocatorias/cursos.html",{'cursos':cursos})

