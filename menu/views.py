from django.shortcuts import render, redirect
from django.views import generic
from menu.models import Ingrediente
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