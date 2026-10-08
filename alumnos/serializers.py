"""
serializers.py — Serializers de la app alumnos (Clase 4 — Django REST Framework).

Un Serializer traduce objetos Django a JSON y JSON a objetos Django,
validando los datos en el proceso. Es el equivalente de ModelForm
pero pensado para APIs en lugar de formularios HTML.
"""

from rest_framework import serializers
from .models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    """
    Serializer del modelo Alumno.

    ModelSerializer genera automáticamente los campos a partir del
    modelo, igual que ModelForm. Reutiliza las validaciones del
    modelo (unique=True, max_length, formato de email, etc.).
    """

    class Meta:
        model = Alumno
        fields = ['id', 'nombre', 'apellido', 'email', 'legajo', 'activo', 'fecha_alta']

        extra_kwargs = {
            # read_only=True: el cliente de la API puede LEER este campo
            # pero no puede enviarlo al crear/editar. Django lo completa solo.
            'fecha_alta': {'read_only': True},
        }
