from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def adoptante(request):
    return render(request, "adoptante.html")

def menu(request):
    return render(request, "menu.html")
    
def lista_mascotas(request):
    mascotas = mascota.objects.all()
    contexto = {
        'mascotas':mascotas
    }
    return render(request, "lista_mascotas.html", contexto)

def crear_mascota(request):
    if request.method == 'GET':
        form = mascotaForm()
        contexto = {
            'form':form
        }
    else:
        form = mascotaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    return render(request,'crear_mascota.html', contexto)

def editar_mascota(request, id):
    Mascota = mascota.objects.get(id=id)
    if request.method == 'GET':
        form = mascotaForm(instance=Mascota)
        contexto = {
            'form':form
        }
    else:
        form = mascotaForm(request.POST, instance=Mascota)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    return render(request, 'crear_mascota.html', contexto)

def eliminar_mascota(request,id):
    Mascota = mascota.objects.get(id=id)
    Mascota.delete() 
    return redirect('lista_mascotas')