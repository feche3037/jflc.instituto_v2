from django.contrib import admin

# Register your models here.

from .models import Inscripcion

@admin.register(Inscripcion)
class AlumnoAdmin(admin.ModelAdmin):
    """Personalización de la vista del modelo Alumno en el admin."""

    list_display = ('fecha_inscripcion', 'nota_final')
    search_fields = ('alumno', 'materias')
    #list_filter = ('alumno', 'materias', 'fecha_inscripcion')
    #readonly_fields = ('fecha_alta',)
    #ordering = ('alumno', 'materias')
