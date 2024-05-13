import requests


def get_pokemon_info(pokemon_name):
    # Base URL of the Pokémon API
    base_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        # Sending a GET request to the API
        response = requests.get(base_url)
        response.raise_for_status()  # Check for HTTP errors

        # Parsing the JSON response
        pokemon_data = response.json()

        # Extracting the desired information
        pokemon_info = {
            "name": pokemon_data["name"].capitalize(),
            "id": pokemon_data["id"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "types": [type_info["type"]["name"] for type_info in pokemon_data["types"]],
            "sprite": pokemon_data["sprites"]["front_default"]
        }

        return pokemon_info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
