from django.contrib import admin
from .models import Cursos


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Cursos)