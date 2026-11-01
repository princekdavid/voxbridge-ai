from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_capabilities_are_explicitly_foundation_only():
    response = client.get("/api/v1/capabilities")
    assert response.status_code == 200
    assert response.json()["pipeline_implemented"] is False
