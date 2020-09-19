"""refugio_mascota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mascota.views import *
from mascota.class_view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ='index'),
    path('adoptante/', adoptante, name ='crear_adoptante'),
    path('menu/', menu, name ='menu'),
    path('lista_mascotas/', lista_mascotas, name ='lista_mascotas'),
    path('crear_mascota/', crear_mascota, name ='crear_mascota'),
    path('editar_mascota/<int:id>', editar_mascota, name ='editar_mascota'),
    path('eliminar_mascota/<int:id>', eliminar_mascota, name ='eliminar_mascota'),
    
    path('lista_adoptantes/', lista_adoptantes.as_view(), name ='lista_adoptantes'),
    path('crear_adoptante/', crear_adoptante.as_view(), name ='crear_adoptante'),
    path('editar_adoptante<int:pk>/', editar_adoptante.as_view(), name ='editar_adoptante'),
    path('eliminar_adoptante<int:pk>/', eliminar_adoptante.as_view(), name ='eliminar_adoptante'),
    path('lista_adopciones/', lista_adopciones.as_view(), name ='lista_adopciones'),
    path('crear_adopcion/', crear_adopcion.as_view(), name ='crear_adopcion'),
    path('editar_adopcion<int:pk>/', editar_adopcion.as_view(), name ='editar_adopcion'),
    path('eliminar_adopcion<int:pk>/', eliminar_adopcion.as_view(), name ='eliminar_adopcion'),
    path('crear_contacto/', crear_contacto.as_view(), name ='crear_contacto'),
    path('lista_contactos/', lista_contactos.as_view(), name ='lista_contactos'),
]

urlpatterns += staticfiles_urlpatterns()