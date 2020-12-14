from typing import Dict

from sqlalchemy.orm import Session
from faker import Factory
from fastapi.testclient import TestClient


from commons.schemas.auth.user import UserCreate
from commons import crud
from commons.config import settings


def create_random_user(db: Session) -> dict:
    faker = Factory.create('pt_BR')
    email = faker.email()
    cpf = faker.cpf().replace('.', '').replace('-', '')
    password = faker.password()
    full_name = faker.first_name() + faker.last_name()

    user_in = UserCreate(email=email, cpf=cpf, password=password, full_name=full_name)

    user = crud.auth.user.user.create(db=db, obj_in=user_in)

    return {"user": user, "email": email, "cpf": cpf, "full_name": full_name, "password": password}


def user_authentication_headers(client: TestClient, email: str, password: str) -> Dict[str, str]:
    data = {"username": email, "password": password}

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers
