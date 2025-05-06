from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_valid_district_profile():
    response = client.get("/district/wa-22/profile")
    assert response.status_code == 200
    data = response.json()
    assert data["district"] == "WA-22"
    assert "population" in data
    assert "demographics" in data
    assert isinstance(data["top_issues"], list)

def test_get_invalid_district_profile():
    response = client.get("/district/fake-99/profile")
    assert response.status_code == 404
    assert response.json()["detail"] == "District profile not found"
