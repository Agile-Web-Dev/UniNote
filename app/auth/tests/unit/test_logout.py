import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import User


@pytest.fixture
def setup(app):
    User.query.delete()

    user = User(
        user_id="123", name="John Doe", email="hello@example.com", role="student"
    )
    user.set_password("password")
    db.session.add(user)
    db.session.commit()

    yield app

    User.query.delete()
    db.session.commit()


def test_logout(client, setup):
    assert next((c for c in client.cookie_jar if "session" == c.name), None) is None
    client.post("/api/auth/login", json={"username": "123", "password": "password"})

    assert next((c for c in client.cookie_jar if "session" == c.name), None) is not None

    response = client.get("/api/auth/logout")

    assert response.status_code == 200
    assert next((c for c in client.cookie_jar if "session" == c.name), None) is None


def test_logout_fail(client, setup):
    assert next((c for c in client.cookie_jar if "session" == c.name), None) is None

    response = client.get("/api/auth/logout")

    assert response.status_code == 401
