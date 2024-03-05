"""
Serialization
- process of translating data structures or objects into a format that
can be stored or transmitted, and then later reconstructed by de-serializing the serialized object.
- useful if we wanna store the state of something for later use
- useful if we are transmitting data across the network
NOTE: When serializing data, we aren't storing objects, we are just storing
the attributes of those objects.
"""
import pickle

starter_pokemons = {"bulbasaur":5, "charmander":5, "squirtle":5}

for pokemon_name, starter_level in starter_pokemons.items():
    print(f"{pokemon_name}: {starter_level}")

serialised_starter_pokemon = pickle.dumps(starter_pokemons)
print(serialised_starter_pokemon)

de_serialised_starter_pokemon = pickle.loads(serialised_starter_pokemon)
print(de_serialised_starter_pokemon)

# Save the serialised binary data in a file
# with open("starter_pokemons.pickle", "wb") as handle:
    # 1st arg: data to be serialized and save
    # 2nd arg: the file to save
    # pickle.dump(starter_pokemons, handle)

# Read the serialised binary data
with open("starter_pokemons.pickle", "rb") as handle:
    deserialied_data = pickle.load(handle)

print(deserialied_data)
