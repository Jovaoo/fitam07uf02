from django.shortcuts import render
from .models import Automobil

def lista_automoviles(request):
    autos = Automobil.objects.all()
    return render(request, 'index.html', {'autos': autos})