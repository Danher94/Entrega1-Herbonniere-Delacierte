from typing import Optional, Type
from django.forms.models import BaseModelForm
from django.shortcuts import render
from inicio.form import BusquedaPoema
from inicio.models import Poema

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')


@login_required
def about(request):
    return render(request, 'inicio/about.html')


def listar_poemas(request):
    
    formulario = BusquedaPoema(request.GET)
    if formulario.is_valid():
        buscar_titulo = formulario.cleaned_data.get('titulo', '')
        lista_poemas = Poema.objects.filter(titulo__icontains=buscar_titulo)
    
    formulario = BusquedaPoema()
    return render(request, 'inicio/poemas.html', {'formulario': formulario, 'lista_poemas': lista_poemas})


class CrearFormPoema(LoginRequiredMixin, CreateView):
    model = Poema
    fields = ['autor', 'titulo', 'contenido', 'fecha_publicacion', 'portada']
    template_name = "inicio/crear_poema.html"
    success_url = reverse_lazy('inicio:poemas')
    
    def get_form(self, form_class=None):
        form = super(CrearFormPoema, self).get_form(form_class)
        form.fields['fecha_publicacion'].widget = forms.DateInput(attrs={'type':'date'})
        return form



class DetallePoema(DetailView):
    model = Poema
    template_name = "inicio/detalle_poema.html"



class ModificarPoema(LoginRequiredMixin, UpdateView):
    model = Poema
    fields = ['autor', 'titulo', 'contenido', 'fecha_publicacion', 'portada']
    template_name = "inicio/modificar_poema.html"
    success_url = reverse_lazy('inicio:poemas')
    
    def get_form(self, form_class=None):
        form = super(ModificarPoema, self).get_form(form_class)
        form.fields['fecha_publicacion'].widget = forms.DateInput(attrs={'type':'date'})
        return form


class EliminarPoema(LoginRequiredMixin, DeleteView):
    model = Poema
    template_name = "inicio/eliminar_poema.html"
    success_url = reverse_lazy('inicio:poemas')
