from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

class lista_adoptantes(ListView):
    model = adoptante
    template_name = 'lista_adoptantes.html'

class crear_adoptante(CreateView):
    model = adoptante
    form_class = adoptanteForm
    template_name = 'crear_adoptante.html'
    success_url = reverse_lazy('index')
   
class editar_adoptante(UpdateView):
    model = adoptante
    form_class = adoptanteForm
    template_name = 'crear_adoptante.html'
    success_url = reverse_lazy('lista_adoptantes')

class eliminar_adoptante(DeleteView):
    model = adoptante
    template_name = 'verificacion.html'
    success_url = reverse_lazy('lista_adoptantes')

#Adopciones

class lista_adopciones(ListView):
    model = historial_mascota
    template_name = 'lista_adopciones.html'

class crear_adopcion(CreateView):
    model = historial_mascota
    form_class = historial_mascotaForm
    template_name = 'crear_adopcion.html'
    success_url = reverse_lazy('lista_adopciones')
   
class editar_adopcion(UpdateView):
    model = historial_mascota
    form_class = historial_mascotaForm
    template_name = 'crear_adopcion.html'
    success_url = reverse_lazy('lista_adopciones')

class eliminar_adopcion(DeleteView):
    model = historial_mascota
    template_name = 'verificacion.html'
    success_url = reverse_lazy('lista_adopciones')

#Contacto
class lista_contactos(ListView):
    model = contacto
    template_name = 'lista_contactos.html'

class crear_contacto(CreateView):
    model = contacto
    form_class = contactoForm
    template_name = 'crear_contacto.html'
    success_url = reverse_lazy('index')
