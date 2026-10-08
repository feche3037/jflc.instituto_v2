"""
models.py — Modelos de la app alumnos.

Un modelo en Django es una clase Python que representa una tabla
en la base de datos. Django se encarga de crear y modificar la
tabla con las migraciones: nunca escribimos SQL a mano para esto.
"""

from django.db import models


class Alumno(models.Model):
    """
    Representa un alumno del Instituto Superior del Milagro.
    """

    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )

    apellido = models.CharField(
        max_length=100,
        verbose_name='Apellido'
    )

    # unique=True: no pueden existir dos alumnos con el mismo email.
    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico'
    )

    # unique=True: legajo irrepetible.
    legajo = models.IntegerField(
        unique=True,
        verbose_name='Legajo'
    )

    activo = models.BooleanField(
        default=True,
        verbose_name='¿Activo?'
    )

    # auto_now_add=True: Django llena este campo automáticamente
    # con la fecha y hora en que se crea el registro.
    fecha_alta = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de alta'
    )

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        """
        Representación legible del objeto. Django la usa en el panel
        de administración y en los templates con {{ alumno }}.
        """
        return f'{self.apellido}, {self.nombre} (Legajo: {self.legajo})'

    def nombre_completo(self):
        """Método auxiliar que devuelve el nombre completo."""
        return f'{self.nombre} {self.apellido}'
