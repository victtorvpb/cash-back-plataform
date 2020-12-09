from fastapi.testclient import TestClient
from http import HTTPStatus


def test_its_alive(client: TestClient):
    data = {'status': 'its_alive'}
    response = client.get('its-alive')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == data
