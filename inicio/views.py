from django.shortcuts import render
from inicio.fomrs import CrearPoema, BusquedaPoema
from inicio.models import Poema

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')



def listar_poemas(request):
    
    formulario = BusquedaPoema(request.GET)
    if formulario.is_valid():
        buscar_titulo = formulario.cleaned_data.get('titulo', '')
        lista_poemas = Poema.objects.filter(titulo__icontains=buscar_titulo)
    
    formulario = BusquedaPoema()
    return render(request, 'inicio/poemas.html', {'formulario': formulario, 'lista_poemas': lista_poemas})



def crear_poema(request):
    
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearPoema(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            poema = Poema(autor=info['autor'],titulo=info['titulo'],fecha_publicacion=info['fecha_publicacion'],portada=info['portada'])
            poema.save()
            mensaje = f'Se creo el poema {poema.titulo}'
        else:
            return render(request, 'inicio/crear_poema.html', {'formulario': formulario})    
    formulario = CrearPoema()
    return render(request, 'inicio/crear_poema.html', {'formulario': formulario, 'mensaje': mensaje})



class DetallePoema(DetailView):
    model = Poema
    template_name = "inicio/detalle_poema.html"


class ModificarPoema(UpdateView):
    model = Poema
    fields = ['autor', 'titulo', 'fecha_publicacion', 'portada']
    template_name = "inicio/modificar_poema.html"
    success_url = reverse_lazy('inicio:poemas')


class EliminarPoema(DeleteView):
    model = Poema
    template_name = "inicio/eliminar_poema.html"
    success_url = reverse_lazy('inicio:poemas')
