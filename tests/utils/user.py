from sqlalchemy.orm import Session
from faker import Factory


from commons.schemas.auth.user import UserCreate
from commons import models, crud


def create_random_user(db: Session) -> models.User:
    faker = Factory.create('pt_BR')
    email = faker.email()
    cpf = faker.cpf()
    password = faker.password()
    full_name = faker.first_name() + faker.last_name()

    user_in = UserCreate(email=email, cpf=cpf, password=password, full_name=full_name)

    user = crud.auth.user.user.create(db=db, obj_in=user_in)

    return user
