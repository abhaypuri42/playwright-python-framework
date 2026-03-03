import pytest

def test_pokemon_api(page):
    response = page.request.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    assert response.status == 200
    data = response.json()
    assert data['name'] == 'pikachu'
    assert data['weight'] == 60
    assert data['abilities'][0]['ability']['name'] == 'static'