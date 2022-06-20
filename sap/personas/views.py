from django.shortcuts import render, get_object_or_404


# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    # detPersona = Persona.objects.get(pk=id)
    detPersona = get_object_or_404(Persona, pk=id)
    return render(request, 'persona/detalle.html', {'dPersona': detPersona})
