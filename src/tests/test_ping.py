def test_ping(test_backend):
    response = test_backend.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}
