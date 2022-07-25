from django.shortcuts import render
from .forms import FamiliaForm

# Create your views here.

def crear_familiares(request):

    formulario=FamiliaForm

    return render(request, 'familia/formulario.html', {'form':formulario})