from django.shortcuts import render,get_object_or_404
from .models import Pokemon
from .forms import PokemonForm
from .pokeapi import get_pokemon

def listar_pokemons(request):
    pokemons = Pokemon.objects.all().order_by('id_pokemon')
    return render(request, 'listar_pokemons.html',{'pokemons':pokemons})

def criar_pokemons(request):
    form = PokemonForm()
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon_name = form.cleaned_data['nome']
            pokemon_info = get_pokemon(pokemon_name)
            if pokemon_info:
                pokemon = Pokemon(
                    id_pokemon = pokemon_info['id'],
                    name = pokemon_info['name'],
                    types = 
                )
