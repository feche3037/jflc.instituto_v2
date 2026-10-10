"""
urls.py — Rutas del sitio web HTML de la app inscripciones.
"""

from django.urls import path
from . import views

app_name = 'inscripciones'

urlpatterns = [
    path('', views.lista_inscripciones, name='lista'),
    path('nueva/', views.alta_inscripcion, name='alta'),
]
