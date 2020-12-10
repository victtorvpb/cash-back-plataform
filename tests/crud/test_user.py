from typing import Generator

from sqlalchemy.orm import Session


from commons import crud
from commons.schemas.auth.user import UserCreate


def test_create_user(db: Session, faker: Generator) -> None:
    email = faker.email()
    cpf = faker.cpf()
    password = faker.password()
    full_name = faker.first_name() + faker.last_name()

    user_in = UserCreate(email=email, cpf=cpf, password=password, full_name=full_name)

    user = crud.auth.user.user.create(db=db, obj_in=user_in)

    assert user.email == email
    assert hasattr(user, "hashed_password")
