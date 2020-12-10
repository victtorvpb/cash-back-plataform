from fastapi import status
from fastapi.testclient import TestClient


def test_its_alive(client: TestClient):
    data = {'status': 'its_alive'}
    response = client.get('its-alive')

    assert response.status_code == status.HTTP_200_OK

    assert response.json() == data
