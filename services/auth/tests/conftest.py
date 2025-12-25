import pytest
from fastapi.testclient import TestClient
from src.run import app
from shared.database import Database
from src.settings import _DB_URL


@pytest.fixture(scope="session")
def client():
    Database.init(_DB_URL)
    return TestClient(app)
