"""
api_views.py — Vistas de la API REST (Clase 4 — Django REST Framework).

Usamos ModelViewSet, que combina automáticamente las operaciones:
  list()    → GET  /api/alumnos/
  create()  → POST /api/alumnos/
  retrieve()→ GET  /api/alumnos/{id}/
  update()  → PUT  /api/alumnos/{id}/
  destroy() → DELETE /api/alumnos/{id}/

Todo el CRUD de la API queda resuelto en pocas líneas, en lugar de
escribir cada vista a mano (como se hace con APIView).
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Alumno
from .serializers import AlumnoSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    """
    ViewSet que expone el CRUD completo de Alumno como API REST.
    """
    queryset = Alumno.objects.all().order_by('apellido', 'nombre')
    serializer_class = AlumnoSerializer

    # Por defecto, DRF identifica cada alumno por su PK interno (id).
    # Usamos 'legajo' en su lugar para que las URLs de la API sean
    # consistentes con las URLs del sitio web HTML
    # (/alumnos/1001/ y /api/alumnos/1001/ apuntan al mismo alumno).
    lookup_field = 'legajo'

    # @action agrega un endpoint personalizado además del CRUD estándar.
    # detail=False → no recibe un id, actúa sobre la colección completa.
    # Resultado: GET /api/alumnos/activos/
    @action(detail=False, methods=['get'], url_path='activos')
    def activos(self, request):
        """Devuelve solamente los alumnos activos."""
        alumnos = Alumno.objects.filter(activo=True).order_by('apellido')
        serializer = self.get_serializer(alumnos, many=True)
        return Response(serializer.data)
