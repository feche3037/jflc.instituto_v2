from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MateriaForm
from .models import Materia

# Create your views here.


def lista_materias(request):
    """
    Muestra todas las materias en una tabla HTML.

    Buscador con Q Objects: el parámetro GET ?q= busca en
    nombre, código o descripción al mismo tiempo (OR).
    """
    termino = request.GET.get("q", "").strip()

    if termino:
        # Q Objects: el | (pipe) combina las condiciones con OR.
        # Sin Q Objects, filter() solo permite combinar con AND.
        materias = Materia.objects.filter(
            Q(nombre__icontains=termino)
            | Q(codigo__icontains=termino)
            | Q(descripcion__icontains=termino)
        ).order_by("codigo")
    else:
        materias = Materia.objects.all().order_by("codigo")

    contexto = {
        "materias": materias,
        "cantidad": materias.count(),
        "termino": termino,
        "titulo": "Listado de Materias",
    }
    return render(request, "materias/lista.html", contexto)


def detalle_materia(request, codigo):
    """Muestra los datos de una materia y los alumnos inscriptos."""
    materia = get_object_or_404(Materia, codigo=codigo)
    return render(request, "materias/detalle.html", {"materia": materia})


@login_required
def alta_materia(request):
    """
    Muestra el formulario de alta (GET) y procesa el envío (POST).

    Patrón POST-Redirect-GET: si el POST es válido, guardamos y
    redirigimos al listado. Así, si el usuario presiona F5, no se
    reenvía el formulario y no se duplican registros.

    @login_required: si el usuario no está logueado, Django lo
    redirige automáticamente a LOGIN_URL (configurado en settings.py).
    """
    if request.method == "POST":
        form = MateriaForm(request.POST)

        if form.is_valid():
            materia = form.save()
            messages.success(
                request, f"✅ Materia {materia.nombre} dada de alta correctamente."
            )
            return redirect("materias:lista")

        messages.error(request, "⚠ Corregí los errores indicados.")

    else:
        form = MateriaForm()

    return render(
        request,
        "materias/form.html",
        {
            "form": form,
            "titulo": "Dar de alta una materia",
            "accion": "Guardar materia",
        },
    )


@login_required
def editar_materia(request, codigo):
    """
    Muestra el formulario pre-cargado con los datos de la materia (GET)
    y procesa los cambios (POST).
    """
    materia = get_object_or_404(Materia, codigo=codigo)

    if request.method == "POST":
        # instance=materia: le decimos al formulario que está editando
        # un registro existente, no creando uno nuevo.
        form = MateriaForm(request.POST, instance=materia)

        if form.is_valid():
            form.save()
            messages.success(
                request, f"✅ Datos de {materia.nombre} actualizados correctamente."
            )
            return redirect("materias:detalle", codigo=materia.codigo)

        messages.error(request, "⚠ Corregí los errores indicados.")

    else:
        form = MateriaForm(instance=materia)

    return render(
        request,
        "materias/form.html",
        {
            "form": form,
            "materia": materia,
            "titulo": f"Editar materia: {materia.nombre}",
            "accion": "Guardar cambios",
        },
    )


@login_required
def baja_materia(request, codigo):
    """
    Muestra una pantalla de confirmación (GET) y elimina el registro (POST).
    Nunca eliminamos en un GET: evita que un link malicioso borre datos
    sin confirmación del usuario.
    """
    materia = get_object_or_404(Materia, codigo=codigo)

    if request.method == "POST":
        nombre = materia.nombre
        materia.delete()
        messages.success(request, f"🗑 Materia {nombre} eliminada correctamente.")
        return redirect("materias:lista")

    return render(request, "materias/confirmar_baja.html", {"materia": materia})
