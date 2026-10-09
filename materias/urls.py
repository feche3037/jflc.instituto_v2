"""
urls.py — Rutas del sitio web HTML de la app materias.

app_name define el namespace: permite usar {% url 'materias:lista' %}
en los templates sin importar cómo esté montada la URL en el proyecto.
"""

from django.urls import path
from . import views

app_name = 'materias' 

urlpatterns = [
    path('', views.lista_materias, name='lista'),
    path('nuevo/', views.alta_materia, name='alta'),
    path('<str:codigo>/', views.detalle_materia, name='detalle'),
    path('<str:codigo>/editar/', views.editar_materia, name='editar'),
    path('<str:codigo>/eliminar/', views.baja_materia, name='baja'),
]
