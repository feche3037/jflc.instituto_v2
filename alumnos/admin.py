"""
admin.py — Registro del modelo Alumno en el panel de administración.

El panel de Django Admin (http://127.0.0.1:8000/admin/) permite
gestionar los datos desde una interfaz web sin escribir código adicional.
"""

from django.contrib import admin
from .models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    """Personalización de la vista del modelo Alumno en el admin."""

    list_display = ('legajo', 'apellido', 'nombre', 'email', 'activo', 'fecha_alta')
    search_fields = ('apellido', 'nombre', 'email', 'legajo')
    list_filter = ('activo',)
    readonly_fields = ('fecha_alta',)
    ordering = ('apellido', 'nombre')
