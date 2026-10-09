"""
views.py — Vistas de la app alumnos (sitio web HTML).

CRUD completo más las funcionalidades de la Clase 4:
  - lista_alumnos  → READ (todos) + buscador con Q Objects + estadísticas con aggregate()
  - detalle_alumno → READ (uno)
  - alta_alumno    → CREATE (protegida con @login_required)
  - editar_alumno  → UPDATE (protegida con @login_required)
  - baja_alumno    → DELETE (protegida con @login_required)
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count

from .models import Alumno
from .forms import AlumnoForm


# ─────────────────────────────────────────────────────────────
# LISTADO — READ (todos) + buscador (Q Objects) + estadísticas (aggregate)
# URL: /alumnos/   name='lista'
# ─────────────────────────────────────────────────────────────

def lista_alumnos(request):
    """
    Muestra todos los alumnos en una tabla HTML.

    Novedades de la Clase 4:
      - Buscador con Q Objects: el parámetro GET ?q= busca en
        nombre, apellido o email al mismo tiempo (OR).
      - Estadísticas con aggregate(): total, activos e inactivos,
        calculadas en una sola consulta a la base de datos.
    """
    termino = request.GET.get('q', '').strip()

    if termino:
        # Q Objects: el | (pipe) combina las condiciones con OR.
        # Sin Q Objects, filter() solo permite combinar con AND.
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=termino) |
            Q(apellido__icontains=termino) |
            Q(email__icontains=termino)
        )
    else:
        alumnos = Alumno.objects.all()

    # aggregate(): calcula varios valores en una sola consulta SQL,
    # sin necesidad de traer todos los registros a Python.
    estadisticas = Alumno.objects.aggregate(
        total=Count('id'),
        activos=Count('id', filter=Q(activo=True)),
        inactivos=Count('id', filter=Q(activo=False)),
    )

    contexto = {
        'alumnos':       alumnos,
        'cantidad':      alumnos.count(),
        'termino':       termino,
        'estadisticas':  estadisticas,
        'titulo':        'Listado de alumnos',
    }
    return render(request, 'alumnos/lista.html', contexto)


# ─────────────────────────────────────────────────────────────
# DETALLE — READ (un alumno)
# URL: /alumnos/<int:legajo>/   name='detalle'
# ─────────────────────────────────────────────────────────────

def detalle_alumno(request, legajo):
    """
    Muestra todos los datos de un alumno identificado por su legajo,
    junto con las materias en las que está inscripto.
    get_object_or_404 devuelve una página 404 amigable si no existe.
    """
    alumno = get_object_or_404(Alumno, legajo=legajo)
    inscripciones = alumno.inscripciones.select_related('materia')
    return render(request, 'alumnos/detalle.html', {
        'alumno':        alumno,
        'inscripciones': inscripciones,
    })


# ─────────────────────────────────────────────────────────────
# ALTA — CREATE
# URL: /alumnos/nuevo/   name='alta'
# Protegida: solo usuarios logueados pueden dar de alta (Clase 4 — Seguridad)
# ─────────────────────────────────────────────────────────────

@login_required
def alta_alumno(request):
    """
    Muestra el formulario de alta (GET) y procesa el envío (POST).

    Patrón POST-Redirect-GET: si el POST es válido, guardamos y
    redirigimos al listado. Así, si el usuario presiona F5, no se
    reenvía el formulario y no se duplican registros.

    @login_required: si el usuario no está logueado, Django lo
    redirige automáticamente a LOGIN_URL (configurado en settings.py).
    """
    if request.method == 'POST':
        form = AlumnoForm(request.POST)

        if form.is_valid():
            alumno = form.save()
            messages.success(
                request,
                f'✅ Alumno {alumno.nombre_completo()} dado de alta correctamente.'
            )
            return redirect('alumnos:lista')

        messages.error(request, '⚠ Corregí los errores indicados.')

    else:
        form = AlumnoForm()

    return render(request, 'alumnos/form.html', {
        'form':   form,
        'titulo': 'Dar de alta un alumno',
        'accion': 'Guardar alumno',
    })


# ─────────────────────────────────────────────────────────────
# EDICIÓN — UPDATE
# URL: /alumnos/<int:legajo>/editar/   name='editar'
# Protegida: solo usuarios logueados pueden editar (Clase 4 — Seguridad)
# ─────────────────────────────────────────────────────────────

@login_required
def editar_alumno(request, legajo):
    """
    Muestra el formulario pre-cargado con los datos del alumno (GET)
    y procesa los cambios (POST).
    """
    alumno = get_object_or_404(Alumno, legajo=legajo)

    if request.method == 'POST':
        # instance=alumno: le decimos al formulario que está editando
        # un registro existente, no creando uno nuevo.
        form = AlumnoForm(request.POST, instance=alumno)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'✅ Datos de {alumno.nombre_completo()} actualizados correctamente.'
            )
            return redirect('alumnos:detalle', legajo=alumno.legajo)

        messages.error(request, '⚠ Corregí los errores indicados.')

    else:
        form = AlumnoForm(instance=alumno)

    return render(request, 'alumnos/form.html', {
        'form':   form,
        'alumno': alumno,
        'titulo': f'Editar alumno: {alumno.nombre_completo()}',
        'accion': 'Guardar cambios',
    })


# ─────────────────────────────────────────────────────────────
# BAJA — DELETE
# URL: /alumnos/<int:legajo>/eliminar/   name='baja'
# Protegida: solo usuarios logueados pueden eliminar (Clase 4 — Seguridad)
# ─────────────────────────────────────────────────────────────

@login_required
def baja_alumno(request, legajo):
    """
    Muestra una pantalla de confirmación (GET) y elimina el registro (POST).
    Nunca eliminamos en un GET: evita que un link malicioso borre datos
    sin confirmación del usuario.
    """
    alumno = get_object_or_404(Alumno, legajo=legajo)

    if request.method == 'POST':
        nombre = alumno.nombre_completo()
        alumno.delete()
        messages.success(request, f'🗑 Alumno {nombre} eliminado correctamente.')
        return redirect('alumnos:lista')

    return render(request, 'alumnos/confirmar_baja.html', {'alumno': alumno})
