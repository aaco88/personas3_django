from django.shortcuts import render, get_object_or_404


# Create your views here.
from personas.models import Domicilio


def detalleDomicilio(request, id):
    detDomicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilio/detalle.html', {'dDomicilio': detDomicilio})
