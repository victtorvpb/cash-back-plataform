import sys
import pytest

import mock

from typing import Generator

from fastapi.testclient import TestClient
from faker import Factory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path = ['', '..'] + sys.path[1:]  # noqa:E402
from commons.db.base import SQLAlchemyBaseModel  # noqa:E402
from main import create_app  # noqa:E402
from resources.deps import get_db  # noqa:E402


SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://tom:tom123@service.postgres:5432/cashback_postgres_test"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


SQLAlchemyBaseModel.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app = create_app()
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def faker() -> Generator:
    return Factory.create('pt_BR')


@pytest.fixture(scope="session")
def db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def mock_response(
    status: int = 200,
    content: str = "CONTENT",
    json_data: dict = None,
    raise_for_status: Exception = None,
):
    mock_resp = mock.Mock()
    mock_resp.raise_for_status = mock.Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status

    mock_resp.status_code = status
    mock_resp.content = content
    if json_data:
        mock_resp.json = mock.Mock(return_value=json_data)
    return mock_resp
