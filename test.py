import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_all_characters():
    response = requests.get(f"{BASE_URL}/characters?limit=20")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 20


def test_specific_character():
    response = requests.get(f"{BASE_URL}/characters/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


def test_filtered_characters():
    response = requests.get(f"{BASE_URL}/characters?house=stark&age_more_than=20")
    assert response.status_code == 200
    data = response.json()
    for character in data:
        assert character['house'].lower() == 'stark'
        assert character['age'] >= 20


def test_sorted_characters():
    response = requests.get(f"{BASE_URL}/characters?sort_asc=name")
    assert response.status_code == 200
    data = response.json()
    names = [character['name'] for character in data]
    assert names == sorted(names)


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
    assert response.status_code == 204
    # Verify that the character is actually deleted
    response = requests.get(f"{BASE_URL}/characters/1")
    assert response.status_code == 404