"""
forms.py — Formularios de la app alumnos.

ModelForm genera automáticamente los campos del formulario a partir
del modelo, incluyendo todas las validaciones definidas en él
(unique=True, max_length, formato de email, etc.).
"""

from django import forms
from .models import Materia


class MateriaForm(forms.ModelForm):
    """
    Formulario para crear y editar alumnos.

    Se usa tanto en la vista alta_alumno (POST con instance=None)
    como en editar_alumno (POST con instance=alumno_existente).
    Django detecta automáticamente si debe hacer INSERT o UPDATE.
    """

    class Meta:
        model = Materia
        fields = ['nombre', 'codigo', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'codigo': 'Codigo',
            'descripcion':    'Descripcion de la Materia',
        }

        help_texts = {
            'codigo': 'Número entero único. Ej: 1001',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ana',
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1001',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Ingresa una descripcion',
                'autocomplete': 'off'
            }),
        }
    # def clean_legajo(self):
    #     """
    #     Validación personalizada del campo legajo.
    #     Se ejecuta automáticamente cuando se llama a form.is_valid().
    #     """
    #     legajo = self.cleaned_data.get('legajo')
    #     if legajo is not None and legajo < 1:
    #         raise forms.ValidationError(
    #             'El legajo debe ser un número entero positivo (mayor a 0).'
    #         )
    #     return legajo
