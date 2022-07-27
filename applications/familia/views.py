from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import FamiliaForm
from .models import Familia
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


 