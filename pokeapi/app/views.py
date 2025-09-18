from django.shortcuts import render,redirect,get_object_or_404
from .models import Pokemon
from .forms import PokemonForm
from .pokeapi import get_pokemon

def listar_pokemons(request):
    pokemons = Pokemon.objects.all().order_by('id_pokemon')
    return render(request, 'listar_pokemons.html',{'pokemons':pokemons})

def criar_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon_name = form.cleaned_data['name']
            pokemon_info = get_pokemon(pokemon_name)
            if pokemon_info:
                pokemon = Pokemon(
                    id_pokemon = pokemon_info['id'],
                    name = pokemon_info['name'],
                    types = "|".join([t["type"]["name"] for t in pokemon_info["types"]]),
                    height = pokemon_info['height'],
                    weight = pokemon_info['weight'],
                    image_url = pokemon_info["sprites"]["front_default"],
                )
                pokemon.save()
                return redirect('listar_pokemons')
    else:
        form = PokemonForm()
    return render(request,'criar_pokemon.html',{'form':form})

def deletar_pokemon(request,pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    pokemon.delete()
    return redirect('listar_pokemons')

def atualizar_pokemon(request,pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST,instance=pokemon)
        if form.is_valid():
            pokemon_name = form.cleaned_data['name']
            pokemon_info = get_pokemon(pokemon_name)
            if pokemon_info:  
                pokemon.id_pokemon = pokemon_info['id']
                pokemon.name = pokemon_info['name']
                pokemon.types = "|".join([t["type"]["name"] for t in pokemon_info["types"]])
                pokemon.height = pokemon_info['height']
                pokemon.weight = pokemon_info['weight']
                pokemon.image_url = pokemon_info["sprites"]["front_default"]
                pokemon.save()
                return redirect('listar_pokemons')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request,'criar_pokemon.html',{'form':form})

def detalhar_pokemon(request,pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request,'detalhar_pokemon.html',{'pokemon':pokemon})