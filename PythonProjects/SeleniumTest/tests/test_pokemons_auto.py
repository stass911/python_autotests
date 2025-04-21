import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'a631a69af9d924de536f555db444f871'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33220'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers',  headers = HEADER)
    assert response.status_code == 200

def test_trainer_id():
    response_get_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID},  headers = HEADER)
    assert response_get_trainers.json()["data"][0]["id"] == "33220"
#Ура! Работает!
    