import requests

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
pokemon_id = response_create.json()['id'] # Переменная созданного покемона
print(pokemon_id) # Вывести переменную созданного покемон

body_add_pokeball = {
    "pokemon_id": '{}'.format(pokemon_id)
}
print(body_add_pokeball)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball) # Поймать в покеболл
print(response_add_pokeball.text)


response_get_trainers = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball' : 1}, headers = HEADER) # Запрос на вывод списка покемонов, готовых к битве
enemy_pokemon_id = response_get_trainers.json()["data"][3]["id"] # Переменная вражеского покемона (3 в списке)

body_battle = {
    "attacking_pokemon": '{}'.format(pokemon_id),
    "defending_pokemon": '{}'.format(enemy_pokemon_id)
}
response_battle = requests.post(url = f'{URL}/battle', headers = HEADER, json = body_battle) # Битва покемонов
print(response_battle.text) # Вывести текст ответа

result_battle = response_battle.json()["result"]
print(result_battle)
