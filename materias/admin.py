from django.contrib import admin

# Register your models here.

from .models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    """Personalización de la vista del modelo Materia en el admin."""

    list_display = ('nombre', 'codigo', 'descripcion')
    search_fields = ('nombre', 'codigo')
    ordering = ('nombre', 'codigo')
