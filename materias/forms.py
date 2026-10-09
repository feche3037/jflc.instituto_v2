"""
forms.py — Formularios de la app materias.

ModelForm genera automáticamente los campos del formulario a partir
del modelo, incluyendo todas las validaciones definidas en él
(unique=True, max_length, formato de email, etc.).
"""

from django import forms
from .models import Materia


class MateriaForm(forms.ModelForm):
    """
    Formulario para crear y editar materias.

    Se usa tanto en la vista alta_materia (POST con instance=None)
    como en editar_materia (POST con instance=materia_existente).
    Django detecta automáticamente si debe hacer INSERT o UPDATE.
    """

    class Meta:
        model = Materia
        fields = ['nombre', 'codigo', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'codigo': 'Código',
            'descripcion': 'Descripción de la materia',
        }

        help_texts = {
            'codigo': 'Código único de la materia. Ej: 1001',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Programación I',
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1001',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá una descripción',
            }),
        }
