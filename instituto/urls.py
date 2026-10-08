"""
urls.py — Tabla de rutas principal del proyecto instituto.

Incluye tres grupos de URLs:
  - /admin/   → panel de administración de Django
  - /alumnos/ → sitio web HTML (vistas FBV con templates)
  - /api/     → API REST en JSON (Django REST Framework, Clase 4)
  - /         → redirige al listado de alumnos
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Sitio web HTML — vistas tradicionales con render()
    path('alumnos/', include('alumnos.urls')),
    path('materias/', include('materias.urls')), 

    # API REST — Clase 4, devuelve JSON en lugar de HTML
    path('api/', include('alumnos.api_urls')),
    # path('api/', include('materias.api_urls')),

    # Redirige la raíz del sitio ("/") al listado de alumnos.
    # Usamos RedirectView en lugar de incluir alumnos.urls otra vez,
    # para no duplicar el namespace 'alumnos'.
    path('', RedirectView.as_view(url='/alumnos/', permanent=False)),
]
