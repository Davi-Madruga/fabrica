from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name']
        widgets = {
            'nome' : forms.TextInput(),
        }
        labels = {
            'nome' : 'Nome',
        }