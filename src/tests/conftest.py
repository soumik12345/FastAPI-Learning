import pytest
from starlette.testclient import TestClient
from backend.main import backend


@pytest.fixture(scope='module')
def test_backend():
    client = TestClient(backend)
    yield client
