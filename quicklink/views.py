from django.shortcuts import render
from .getpokemon import get_pokemon_info
# Create your views here.
def go_pokemon(request, pokemon_name):
    pokemon_info = get_pokemon_info(pokemon_name)

    context = {
        "pokemon": pokemon_info
    }

    return render(request, "quicklink/pokemon.html", context)