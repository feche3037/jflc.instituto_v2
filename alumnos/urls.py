"""
urls.py — Rutas del sitio web HTML de la app alumnos.

app_name define el namespace: permite usar {% url 'alumnos:lista' %}
en los templates sin importar cómo esté montada la URL en el proyecto.
"""

from django.urls import path
from . import views

app_name = 'alumnos' 

urlpatterns = [
    path('', views.lista_alumnos, name='lista'),
    path('nuevo/', views.alta_alumno, name='alta'),
    path('<int:legajo>/', views.detalle_alumno, name='detalle'),
    path('<int:legajo>/editar/', views.editar_alumno, name='editar'),
    path('<int:legajo>/eliminar/', views.baja_alumno, name='baja'),
]
