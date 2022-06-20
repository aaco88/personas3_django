from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    cantPersonas = Persona.objects.count()
    todasPersonas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'cPersonas': cantPersonas, 'tPersonas': todasPersonas})