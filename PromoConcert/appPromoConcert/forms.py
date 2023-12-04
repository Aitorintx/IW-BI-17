from django import forms
from .models import Interprete, Festival

class InterpreteForm(forms.ModelForm):
    class Meta:
        model = Interprete
        fields = ['nameInterprete', 'infoInterprete']

class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['idFestival', 'nombreFestival', 'infoFestival', 'fecha', 'promotor']
