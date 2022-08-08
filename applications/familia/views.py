from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import FamiliaForm, ZapasForm
from .models import Familia, Zapas
# Create your views here.

def inicio(request):

    return render(request, 'index.html')
    
class FamiliaCreateView(CreateView):
    template_name = "familia/add_familia.html"
    model = Familia
    form_class=FamiliaForm
    success_url=reverse_lazy('familia_app:ListaFamiliares')

 
class FamiliaListView(ListView):
    template_name = "familia/listar.html"
    model = Familia
    context_object_name="lista"


class FamiliaDeleteView(DeleteView):
    model = Familia
    template_name = "familia/delete.html"
    success_url =  reverse_lazy('familia_app:ListaFamiliares')


class FamiliaUpdateView(UpdateView):
    model = Familia
    template_name = "familia/update.html"
    # fields=('__all__')
    form_class=FamiliaForm
    success_url =  reverse_lazy('familia_app:ListaFamiliares')



class ZapasreateView(CreateView):
    model = Zapas
    template_name = "familia/zapas.html"
    form_class=ZapasForm
    success_url=reverse_lazy('familia_app:Listado-zapas')

def mostrar_zapatillas(request):
    zapatillas=Zapas.objects.all()
    return render(request, 'familia/listado-zapatillas.html', {'zapatillas':zapatillas})


class ZapasUpdateView(UpdateView):
    model = Zapas
    template_name = "familia/update-zapas.html"
    form_class=ZapasForm
    success_url =  reverse_lazy('familia_app:Listado-zapas')


def eliminar_zapas(request, id):
    zapas=Zapas.objects.get(id=id)
    zapas.delete()

    return render(request, 'index.html')