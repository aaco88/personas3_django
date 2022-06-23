from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Domicilio


def detalleDomicilio(request, id):
    detDomicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilio/detalle.html', {'dDomicilio': detDomicilio})


DomicilioForm = modelform_factory(Domicilio, exclude=[])


def agregarDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index2')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'domicilio/agregar.html', {'fDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    editDomicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=editDomicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index2')
    else:
        formaDomicilio = DomicilioForm(instance=editDomicilio)
    return render(request, 'domicilio/editar.html', {'fDomicilio': formaDomicilio})