"""
forms.py — Formulario de la app inscripciones.

No es un ModelForm porque una sola acción crea varias inscripciones:
un alumno y una lista de materias.
"""

from django import forms

from alumnos.models import Alumno
from materias.models import Materia


class InscripcionForm(forms.Form):
    alumno = forms.ModelChoiceField(
        queryset=Alumno.objects.filter(activo=True),
        label='Alumno',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    materias = forms.ModelMultipleChoiceField(
        queryset=Materia.objects.all(),
        label='Materias',
        help_text='Seleccioná una o más materias.',
        widget=forms.CheckboxSelectMultiple,
    )
