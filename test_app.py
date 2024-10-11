import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_characters():
    response = requests.get(f"{BASE_URL}/characters?limit=20")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 20


def test_get_character_by_id():
    response = requests.get(f"{BASE_URL}/characters/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


def test_filter_characters():
    response = requests.get(f"{BASE_URL}/characters/filter?house=stark&age_more_than=20")
    assert response.status_code == 200
    data = response.json()
    for character in data:
        assert character['house'].lower() == 'stark'
        assert character['age'] > 20


def test_sorted_characters():
    response = requests.get(f"{BASE_URL}/characters/sorted?sort_field=name&order=asc")
    assert response.status_code == 200
    data = response.json()
    names = [character['name'] for character in data]
    assert names == sorted(names)


def test_add_character():
    new_character = {
        "id": 100,
        "name": "Test Character",
        "house": "Test House",
        "animal": "Test Animal",
        "symbol": "Test Symbol",
        "nickname": "Test Nickname",
        "role": "Test Role",
        "age": 30,
        "death": None,
        "strength": "Test Strength"
    }
    response = requests.post(f"{BASE_URL}/characters", json=new_character)
    assert response.status_code == 201
    assert response.json()['name'] == new_character['name']


def test_edit_character():
    updated_character = {
        "name": "Updated Character",
        "house": "Updated House"
    }
    response = requests.patch(f"{BASE_URL}/characters/1", json=updated_character)
    assert response.status_code == 200
    assert response.json()['house'] == updated_character['house']


def test_delete_character():
    response = requests.delete(f"{BASE_URL}/characters/1")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/characters/1")
    assert response.status_code == 404