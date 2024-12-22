import pytest
from fastapi.testclient import TestClient
from chatroom_data/app import app

client = TestClient(app)

def test_get_anime():
    response = client.get("/anime")
    assert response.status_code == 200
    assert "anime" in response.json()

def test_get_chat_history():
    anime_id = 1
    response = client.get(f"/chat/{anime_id}")
    assert response.status_code == 200
    assert "chat_history" in response.json()  # Fix the typo

