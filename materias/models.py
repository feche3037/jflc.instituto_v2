from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        """
        Representación legible del objeto. Django la usa en el panel
        de administración y en los templates con {{ materia}}.
        """
        return f'{self.codigo}, {self.nombre}'
