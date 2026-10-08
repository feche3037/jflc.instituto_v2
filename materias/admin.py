from django.contrib import admin

# Register your models here.

from .models import Materia

@admin.register(Materia)
class AlumnoAdmin(admin.ModelAdmin):
    """Personalización de la vista del modelo Alumno en el admin."""

    list_display = ('nombre', 'codigo', 'descripcion')
    search_fields = ('nombre', 'codigo')
    list_filter = ('nombre', 'codigo')
    #readonly_fields = ('fecha_alta',)
    ordering = ('nombre', 'codigo')
