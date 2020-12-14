from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from commons.config import settings
from tests.utils.user import create_random_user


def test_get_access_token(db: Session, client: TestClient) -> None:

    dict_user = create_random_user(db)
    login_data = {
        "username": dict_user.get("email"),
        "password": dict_user.get("password"),
    }
    response = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = response.json()
    assert response.status_code == 200
    assert tokens.get('access_token')
