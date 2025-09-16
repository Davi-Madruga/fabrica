import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return False

def get_ataque(name):
    url = f"{base_url}/move/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        ataque_data = response.json
        return ataque_data
    else:
        return False

