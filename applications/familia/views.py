from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import FamiliaForm, ZapasForm
from .models import Familia, Zapas

from .forms import FamiliaForm, MascotasForm
from .models import Familia, Mascotas

# Create your views here.

def inicio(request):

    return render(request, 'index.html')
    
class FamiliaCreateView(CreateView):
    template_name = "familia/add_familia.html"
    model = Familia
    form_class=FamiliaForm
    success_url=reverse_lazy('familia_app:ListaFamiliares')

def buscar_familia(request):
    return render(request, "familia/listar.html")

def buscar(request): 

    if request.GET['nombre']:
        nombre=request.GET['nombre']
        resultado=Familia.objects.filter(nombre__icontains=nombre)
        return render(request, "familia/buscar.html", {"resultado":resultado} )
    else:
        return render(request, "familia/buscar.html")
 
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

######### Mascotas #########
class MascotasListView(ListView):
    model= Mascotas
    template_name = "mascotas/listar.html"
    context_object_name="lista"



class ZapasreateView(CreateView):
    model = Zapas
    template_name = "familia/zapas.html"
    form_class=ZapasForm
    success_url=reverse_lazy('familia_app:Listado-zapas')

def mostrar_zapatillas(request):
    zapatillas=Zapas.objects.all()
    return render(request, 'familia/listado-zapatillas.html', {'zapatillas':zapatillas})


# class ZapasUpdateView(UpdateView):
#     model = Zapas
#     template_name = "familia/update-zapas.html"
#     form_class=ZapasForm
#     success_url =  reverse_lazy('familia_app:Listado-zapas')


def actualizar(request, id):
    zapatillas=Zapas.objects.get(id=id)

    if request.method=="POST":
        formulario=ZapasForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            zapatillas.nombre=informacion['nombre']
            zapatillas.precio=informacion['precio']
            zapatillas.fecha_v=informacion['fecha_v']
            
            
            zapatillas.save()
            return redirect("familia_app:Listado-zapas")

    else:
        formulario = ZapasForm(initial={"nombre":zapatillas.nombre, "precio":zapatillas.precio, "fecha_v":zapatillas.fecha_v})

    return render(request, "familia/update-zapas.html",{"form":formulario})

def eliminar_zapas(request, id):
    zapas=Zapas.objects.get(id=id)
    zapas.delete()

    return render(request, 'index.html')

class MascotaCreateView(CreateView):
    template_name = "mascotas/add_mascota.html"
    model = Mascotas
    form_class=MascotasForm
    success_url=reverse_lazy('familia_app:ListaMascotas')

class MascotaDeleteView(DeleteView):
    template_name = "mascotas/delete.html"
    model = Mascotas
    success_url=reverse_lazy('familia_app:ListaMascotas')

class MascotaUpdateView(UpdateView):
    template_name = "mascotas/update.html"
    model = Mascotas
    form_class=MascotasForm
    success_url=reverse_lazy('familia_app:ListaMascotas')

def searchMascot(request): 

    if request.GET['nombre']:
        nombre=request.GET['nombre']
        resultado=Mascotas.objects.filter(nombre__icontains=nombre)
        return render(request, "mascotas/search.html", {"resultado":resultado} )
    else:
        return render(request, "mascotas/search.html")
