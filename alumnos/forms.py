"""
forms.py — Formularios de la app alumnos.

ModelForm genera automáticamente los campos del formulario a partir
del modelo, incluyendo todas las validaciones definidas en él
(unique=True, max_length, formato de email, etc.).
"""

from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    """
    Formulario para crear y editar alumnos.

    Se usa tanto en la vista alta_alumno (POST con instance=None)
    como en editar_alumno (POST con instance=alumno_existente).
    Django detecta automáticamente si debe hacer INSERT o UPDATE.
    """

    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email', 'legajo', 'activo']

        labels = {
            'nombre':   'Nombre',
            'apellido': 'Apellido',
            'email':    'Correo electrónico',
            'legajo':   'Número de legajo',
            'activo':   '¿Alumno activo?',
        }

        help_texts = {
            'email':  'Ingresá una dirección de correo válida. No puede repetirse.',
            'legajo': 'Número entero único. Ej: 1001',
            'activo': 'Desmarcá si el alumno ya no está cursando.',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ana',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: García',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ana@isdem.edu.ar',
            }),
            'legajo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Ej: 1001',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    def clean_legajo(self):
        """
        Validación personalizada del campo legajo.
        Se ejecuta automáticamente cuando se llama a form.is_valid().
        """
        legajo = self.cleaned_data.get('legajo')
        if legajo is not None and legajo < 1:
            raise forms.ValidationError(
                'El legajo debe ser un número entero positivo (mayor a 0).'
            )
        return legajo
