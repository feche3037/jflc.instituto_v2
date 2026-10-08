#!/usr/bin/env python
"""
manage.py — Script de utilidades de Django.
No modificar este archivo. Se usa desde la terminal para:
  - Arrancar el servidor de desarrollo: python manage.py runserver
  - Crear migraciones:                  python manage.py makemigrations
  - Aplicar migraciones:                python manage.py migrate
  - Crear superusuario:                 python manage.py createsuperuser
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instituto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Verificá que el entorno virtual "
            "esté activado y que Django esté instalado."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
