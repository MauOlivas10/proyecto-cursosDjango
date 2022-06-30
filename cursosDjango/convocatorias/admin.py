from django.contrib import admin
from .models import Cursos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombreCurso', 'nombreProfesor', 'totalLecciones', 'totalHoras', 'clasificacionCurso', 'fechaPublicacion')
    search_fields = ('nombreCurso', 'nombreProfesor', 'totalLecciones', 'totalHoras', 'clasificacionCurso', 'fechaPublicacion')
    date_hierarchy = 'created'
    list_filter = ('nombreCurso', 'nombreProfesor', 'totalLecciones', 'totalHoras', 'clasificacionCurso', 'fechaPublicacion')

admin.site.register(Cursos, AdministrarModelo)



