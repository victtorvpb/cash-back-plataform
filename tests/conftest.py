from typing import Generator

import pytest
from fastapi.testclient import TestClient
from main import create_app


@pytest.fixture(scope="module")
def client() -> Generator:
    app = create_app()
    with TestClient(app) as c:
        yield c
