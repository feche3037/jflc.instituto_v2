"""
settings.py — Configuración principal del proyecto instituto.

Versión Clase 4: usa python-decouple para leer configuración sensible
desde el archivo .env (nunca se sube a git) y agrega Django REST
Framework para la API.
"""

from pathlib import Path
from decouple import config, Csv

# BASE_DIR apunta a la carpeta raíz del proyecto (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent


# ─── SEGURIDAD — TODO esto se lee del archivo .env ──────────────────────────

# Clave secreta usada para firmar cookies y tokens CSRF.
# Ya NO está hardcodeada acá: se lee desde el archivo .env
SECRET_KEY = config('SECRET_KEY')

# DEBUG=True en desarrollo, DEBUG=False en producción.
# cast=bool convierte el texto "True"/"False" del .env a un booleano real.
DEBUG = config('DEBUG', default=False, cast=bool)

# Lista de hosts permitidos, separados por coma en el .env.
# Csv() convierte automáticamente "127.0.0.1,localhost" en una lista.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())


# ─── APLICACIONES INSTALADAS ───────────────────────────────────────────────

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework — agregado en la Clase 4 para la API
    'rest_framework',

    # Nuestra aplicación de gestión de alumnos
    'alumnos',
    'materias',
    'inscripciones',
]


# ─── CONFIGURACIÓN DE DJANGO REST FRAMEWORK ────────────────────────────────

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # BrowsableAPIRenderer agrega la interfaz web para explorar la API
        # desde el navegador. En producción a veces se quita por seguridad.
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}


# ─── MIDDLEWARE ────────────────────────────────────────────────────────────

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ─── URLs ──────────────────────────────────────────────────────────────────

ROOT_URLCONF = 'instituto.urls'


# ─── PLANTILLAS ────────────────────────────────────────────────────────────

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'instituto.wsgi.application'


# ─── BASE DE DATOS ─────────────────────────────────────────────────────────

# SQLite: base de datos en un único archivo, sin instalación adicional.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ─── VALIDACIÓN DE CONTRASEÑAS ─────────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ─── INTERNACIONALIZACIÓN ──────────────────────────────────────────────────

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Salta'
USE_I18N = True
USE_TZ = True


# ─── ARCHIVOS ESTÁTICOS ────────────────────────────────────────────────────

STATIC_URL = '/static/'


# ─── CAMPO PK POR DEFECTO ──────────────────────────────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ─── MENSAJES FLASH ────────────────────────────────────────────────────────

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG:   'debug',
    messages.INFO:    'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR:   'error',
}

# ─── AUTENTICACIÓN ──────────────────────────────────────────────────────────

# A dónde redirige Django cuando una vista protegida con @login_required
# detecta que el usuario no está logueado. Usamos el login del admin
# porque no construimos un login propio en este proyecto.
LOGIN_URL = '/admin/login/'
