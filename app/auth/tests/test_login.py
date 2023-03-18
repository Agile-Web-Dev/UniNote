from app.libs.tests.fixtures import client


def test_request_example():
    response = client.get("/api/ping")
    assert response.json == {"msg": "pong!"}
    assert response.status_code == 200
