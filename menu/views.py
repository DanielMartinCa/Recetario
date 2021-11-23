from django.shortcuts import render, redirect
from django.views import generic
from menu.models import Ingrediente, Receta
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import os # para construir las rutas con os.path
from django.conf import settings #para saber donde están los media


# Create your views here.


def indice(request):
    '''
    Página inicial de la web
    '''
    datos= {'autor': 'Daniel Martín'}
    # ejemplo sesiones
    visitas = request.session.get('visitas', 0)
    request.session['visitas']= visitas + 1
    datos['visitas'] = visitas

    
    
    
    return render(request, 'index.html', context=datos)

class CreaIngrediente(SuccessMessageMixin, generic.CreateView):
    model = Ingrediente
    fields = '__all__'
    template_name = 'crear_ingrediente.html'
    success_url = '/'
    
    success_message = "%(nombre)s %(origen)s se ha creado correctamente"

class CreaReceta(SuccessMessageMixin, generic.CreateView):
    model = Receta
    fields = '__all__'
    template_name = 'crear_receta.html'
    success_url = '/'
    
    success_message = "%(nombre)s se ha creado correctamente"
def subir_archivo(request):
    if request.method == 'POST':
        nombre =request.FILES["file"].name
        save_path = os.path.join(settings.MEDIA_ROOT, nombre)

        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["file"].chunks():
                output_file.write(chunk)
        
        return render(request, 'subir_archivo.html', {'imagen': nombre})
    else:
        return render(request, 'subir_archivo.html')


def todos_ingredientes(request):
    ingredientes = Ingrediente.objects.all().order_by('nombre')
    return render(request, 'listaIngredientes.html', context={'ingredientes':ingredientes})


