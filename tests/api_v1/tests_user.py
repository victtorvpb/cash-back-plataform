from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from commons import crud


from commons.config import settings


def test_create_new_user(db: Session, client: TestClient, faker: Generator) -> None:
    email = faker.email()
    cpf = faker.cpf()
    password = faker.password()
    full_name = faker.first_name() + faker.last_name()

    data = {"email": email, "password": password, "cpf": cpf, "full_name": full_name}
    r = client.post(
        f"{settings.API_V1_STR}/users/",
        json=data,
    )

    assert 200 <= r.status_code < 300
    created_user = r.json()
    user = crud.user.get_by_email_or_cpf(db, email=email, cpf=cpf)
    assert user
    assert user.email == created_user["email"]
