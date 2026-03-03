from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Asalamualeykum"}

def test_sum():
    response = client.get("/sum?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

from fastapi.testclient import TestClient
from main import app

def test_goodbye():
    response = client.get("/Goodbye/Alice")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Goodbye, Alice!"}