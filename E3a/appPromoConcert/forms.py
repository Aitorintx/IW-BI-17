from django import forms
from .models import Interprete, Festival, Contacto, Promotor
from django.contrib.auth.forms import AuthenticationForm

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

class LoginIForm(forms.ModelForm):
    class Meta:
        model=Promotor
        fields= ['namePromotor']

class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(widget=forms.HiddenInput, initial='fakepassword', required=False)
    username = forms.CharField(label='Nombre')
    class Meta:
        model = Promotor
        fields = ['namePromotor']
        widgets = {
        'namePromotor': forms.TextInput(attrs={'placeholder': 'Nombre'}),
        }