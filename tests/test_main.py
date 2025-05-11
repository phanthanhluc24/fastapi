from http.client import responses

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    test_data = {
        "name": "Nguyen Huu Thang",
        "email": "thangnguyen1@gmail.com",
        "password":"1234"
    }

    response = client.post("/api/users",json=test_data)
    assert response.status_code == 200
    assert response.json() == test_data

