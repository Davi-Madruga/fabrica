from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','idade','email']
        widgets = {
            'nome' : forms.TextInput(),
            'idade' : forms.TextInput(),
            'email' : forms.TextInput()
        }
        labels = {
            'nome' : 'Nome',
            'idade' : 'Idade',
            'email' : 'Email'
        }