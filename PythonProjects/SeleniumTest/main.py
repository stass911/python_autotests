import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'a631a69af9d924de536f555db444f871'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
#1
body_creat_pokemons = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat_pokemons) # Создание покемона
print(response_create.text) # Вывести текст ответа

print(response_create.status_code) # Вывести статус код
pokemon_id = response_create.json()['id'] # Переменная созданного покемона
print(pokemon_id) # Вывести переменную созданного покемон

#2
body_add_pokeball = {
    "pokemon_id": "297007"
}
print(body_add_pokeball)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball) # Поймать в покеболл

print(response_add_pokeball.text)

#3
body_rename_pokemons = {
    "pokemon_id": "297007",
    "name": "New Name",
    "photo_id": 666
}

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemons) # Смена имени покемона
print(response_change_name.text)
