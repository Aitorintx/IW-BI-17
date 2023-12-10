from django import forms
from .models import Interprete, Festival, Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono']

class InterpreteForm(forms.ModelForm):
    class Meta:
        model = Interprete
        fields = ['nameInterprete', 'infoInterprete']

class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['idFestival', 'nombreFestival', 'infoFestival', 'fecha', 'promotor']
