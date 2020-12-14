import pytest

from uuid import uuid4
from datetime import datetime

from typing import Generator
from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy.orm import Session

from commons import crud, schemas
from tests.utils.user import create_random_user, user_authentication_headers
from commons.config import settings


values_to_new_purchase = {
    (999, 10),
    (1000, 15),
    (1001, 15),
    (1500, 15),
    (1501, 20),
    (-1, 0),
}


@pytest.mark.parametrize("value_purchase,percente_cashback", values_to_new_purchase)
def test_post_new_purchase(
    db: Session, client: TestClient, faker: Generator, value_purchase: int, percente_cashback: int
) -> None:

    dict_user = create_random_user(db)
    user = dict_user.get('user')
    code = faker.word()
    value = value_purchase
    purchase_date = datetime.now().isoformat()
    cpf = user.cpf
    data = {"code": code, "value": value, "purchase_date": purchase_date, "cpf": cpf}

    headers = user_authentication_headers(client, user.email, dict_user.get('password'))
    response = client.post(f"{settings.API_V1_STR}/purchase", json=data, headers=headers)
    
    assert status.HTTP_200_OK == response.status_code

    created_purchase = response.json()
    request_uuid = str(uuid4())
    purchase = crud.purchase.get_purchase_by_code(db, code=code, request_uuid=request_uuid)
    assert schemas.Pusrchase.parse_obj(created_purchase)
    assert purchase
    assert float(purchase.cashback_percente) == percente_cashback
    assert float(purchase.cashback_value) == value * (percente_cashback / 100)


def test_get_credit(
    db: Session, client: TestClient, faker: Generator) -> None:

    dict_user = create_random_user(db)
    user = dict_user.get('user')
    cpf = user.cpf
 
    headers = user_authentication_headers(client, user.email, dict_user.get('password'))
    response = client.get(f"{settings.API_V1_STR}/credit-delear?reseller_cpf={cpf}", headers=headers)

    assert 200 <= response.status_code < 300

    created_purchase = response.json()

    assert schemas.PurcahseCredit.parse_obj(created_purchase).credit


def test_get_credit_whitout_user(
    db: Session, client: TestClient, faker: Generator) -> None:

    dict_user = create_random_user(db)
    user = dict_user.get('user')
 
    headers = user_authentication_headers(client, user.email, dict_user.get('password'))
    response = client.get(f"{settings.API_V1_STR}/credit-delear?reseller_cpf=teste", headers=headers)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

