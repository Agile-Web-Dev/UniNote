from app.libs.tests.fixtures import app, client


def test_ping(client):
    response = client.get("/api/ping")
    assert response.json == {"msg": "pong!"}
    assert response.status_code == 200
