from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona
from personas.forms import PersonaForm


def detallePersona(request, id):
    # detPersona = Persona.objects.get(pk=id)
    detPersona = get_object_or_404(Persona, pk=id)
    return render(request, 'persona/detalle.html', {'dPersona': detPersona})


# PersonaForm = modelform_factory(Persona, exclude=[])


def agregarPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'persona/agregar.html', {'fPersona': formaPersona})


def editarPersona(request, id):
    editPersona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=editPersona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=editPersona)
    return render(request, 'persona/editar.html', {'fPersona': formaPersona})


def eliminarPersona(request, id):
    elimPersona = get_object_or_404(Persona, pk=id)
    if elimPersona:
        elimPersona.delete()
    return redirect('index')
