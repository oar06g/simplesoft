def test_health(client):
    response = client.get("/auth/health")
    assert response.status_code == 200