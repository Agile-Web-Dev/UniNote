from app.libs.tests.fixtures import app, client


def test_get_notes(client):
    response = client.get("/api/notes")
    assert response.json == {"msg": "pong!"}
    assert response.status_code == 200
