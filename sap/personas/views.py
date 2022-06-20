from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    # detPersona = Persona.objects.get(pk=id)
    detPersona = get_object_or_404(Persona, pk=id)
    return render(request, 'persona/detalle.html', {'dPersona': detPersona})


PersonaForm = modelform_factory(Persona, exclude=[])


def agregarPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'persona/agregar.html', {'fPersona': formaPersona})
