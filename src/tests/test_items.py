from random import random, randint, choices
from string import ascii_lowercase, ascii_uppercase, digits


def test_get_item_int(test_backend):
    item_id = int(digits)
    response = test_backend.get('/items/{}'.format(item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(item_id)}


def test_get_item_random(test_backend):
    random_item_id = random()
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(random_item_id)}


def test_get_item_randint(test_backend):
    random_item_id = randint(-1000, 1000)
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(random_item_id)}


def test_get_item_string(test_backend):
    item_id = ascii_uppercase + digits + ascii_lowercase
    response = test_backend.get('/items/{}'.format(item_id))
    assert response.status_code == 200
    assert response.json() == {'item': item_id}


def test_get_item_random_str(test_backend):
    random_item_id = ''.join(
        choices(
            ascii_uppercase + digits + ascii_lowercase,
            k=randint(10, 100)
        )
    )
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': random_item_id}
