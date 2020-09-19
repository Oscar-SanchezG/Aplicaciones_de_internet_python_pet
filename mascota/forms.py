from django import forms
from .models import *

class mascotaForm(forms.ModelForm):
    class Meta:
        model = mascota
        fields = '__all__'

class adoptanteForm(forms.ModelForm):
    class Meta:
        model = adoptante
        fields = '__all__'

class historial_mascotaForm(forms.ModelForm):
    class Meta:
        model = historial_mascota
        fields = '__all__'

class contactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'