from django import forms
from .models import Interprete

class InterpreteForm(forms.ModelForm):
    class Meta:
        model = Interprete
        fields = ['nameInterprete', 'infoInterprete']
