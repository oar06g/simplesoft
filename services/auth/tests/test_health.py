from fastapi.testclient import TestClient
# from src.run import app
# from shared.database import Database
# from src.settings import _DB_URL

# Database.init(_DB_URL)


# client = TestClient(app)

def test_health(client):
    response = client.get("/auth/health")
    assert response.status_code == 200