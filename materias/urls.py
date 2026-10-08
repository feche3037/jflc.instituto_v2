"""
urls.py — Rutas del sitio web HTML de la app alumnos.

app_name define el namespace: permite usar {% url 'alumnos:lista' %}
en los templates sin importar cómo esté montada la URL en el proyecto.
"""

from django.urls import path
from . import views

app_name = 'materias' 

urlpatterns = [
    path('', views.lista_materias, name='lista'),
    path('nuevo/', views.alta_materia, name='alta'),
    # path('<int:legajo>/', views.detalle_alumno, name='detalle'),
    path('<int:codigo>/editar/', views.editar_materia, name='editar'),
    path('<int:codigo>/eliminar/', views.baja_materia, name='baja'),
]
