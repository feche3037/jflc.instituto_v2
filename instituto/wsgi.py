"""
wsgi.py — Interfaz WSGI del proyecto instituto.
No modificar este archivo.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instituto.settings')
application = get_wsgi_application()
