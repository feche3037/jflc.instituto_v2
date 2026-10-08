"""
api_urls.py — Rutas de la API REST (Clase 4 — Django REST Framework).

DefaultRouter genera automáticamente todas las URLs del CRUD a partir
del ViewSet registrado, sin necesidad de escribir cada path() a mano.

URLs que quedan disponibles después de este registro:
  GET/POST        /api/alumnos/
  GET/PUT/DELETE  /api/alumnos/{id}/
  GET             /api/alumnos/activos/   (endpoint personalizado)
"""

from rest_framework.routers import DefaultRouter
from .api_views import AlumnoViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumno')

urlpatterns = router.urls
