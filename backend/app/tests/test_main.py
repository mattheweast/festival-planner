from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


# Test Home Page GET Method "/"
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my API"}
