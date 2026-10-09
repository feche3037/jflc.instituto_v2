from django.contrib import admin

# Register your models here.

from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    """Personalización de la vista del modelo Inscripcion en el admin."""

    list_display = ('alumno', 'materia', 'estado', 'fecha_inscripcion', 'nota_final')
    search_fields = ('alumno__apellido', 'materia__nombre')
    list_filter = ('estado',)
