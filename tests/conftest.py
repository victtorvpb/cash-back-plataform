import sys
import pytest


from typing import Generator


from fastapi.testclient import TestClient
from faker import Factory

sys.path = ['', '..'] + sys.path[1:]
from commons.db.session import engine, SessionLocal  # noqa
from main import create_app  # noqa


@pytest.fixture(scope="module")
def client() -> Generator:
    app = create_app()
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def faker() -> Generator:
    return Factory.create('pt_BR')

@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()
