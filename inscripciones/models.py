from django.db import models

# Create your models here.
from alumnos.models import Alumno
from materias.models import Materia
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='inscripciones')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    ESTADOS = [
        ('CURSANDO', 'Cursando'),
        ('REGULAR', 'Regular'),
        ('APROBADO', 'Aprobado'),
        ('LIBRE', 'Libre'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='CURSANDO')
    class Meta:
        # Evita que un alumno se inscriba dos veces a la misma materia
        unique_together = ('alumno', 'materia')
    def __str__(self):
        return f"{self.alumno} en {self.materia} ({self.estado})"
