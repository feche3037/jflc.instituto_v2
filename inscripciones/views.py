"""
views.py — Vistas de la app inscripciones (sitio web HTML).

  - lista_inscripciones → READ (todas)
  - alta_inscripcion    → CREATE (un alumno en varias materias)
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import InscripcionForm
from .models import Inscripcion


def lista_inscripciones(request):
    """Muestra todas las inscripciones en una tabla HTML."""
    inscripciones = Inscripcion.objects.select_related("alumno", "materia").order_by(
        "alumno", "materia"
    )
    return render(
        request,
        "inscripciones/lista.html",
        {
            "inscripciones": inscripciones,
            "cantidad": inscripciones.count(),
        },
    )


@login_required
def alta_inscripcion(request):
    """
    Muestra el formulario (GET) y procesa el envío (POST).
    Crea una inscripción por cada materia elegida; las que el alumno
    ya tenía se omiten (unique_together evitaría duplicarlas).
    """
    if request.method == "POST":
        form = InscripcionForm(request.POST)

        if form.is_valid():
            alumno = form.cleaned_data["alumno"]
            nuevas = 0
            for materia in form.cleaned_data["materias"]:
                _, creada = Inscripcion.objects.get_or_create(
                    alumno=alumno, materia=materia
                )
                nuevas += creada

            messages.success(
                request,
                f"✅ {alumno.nombre_completo()} inscripto en {nuevas} materia{'s' if nuevas != 1 else ''}.",
            )
            return redirect("alumnos:detalle", legajo=alumno.legajo)

        messages.error(request, "⚠ Corregí los errores indicados.")

    else:
        # ?alumno=<id> preselecciona el alumno (link desde su detalle).
        form = InscripcionForm(initial={"alumno": request.GET.get("alumno")})

    return render(
        request,
        "inscripciones/form.html",
        {
            "form": form,
            "titulo": "Inscribir alumno en materias",
            "accion": "Inscribir",
        },
    )
