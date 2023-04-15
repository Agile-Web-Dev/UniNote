import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import User


@pytest.fixture
def setup(app):
    with app.app_context():
        User.query.delete()

        user = User(
            user_id="123", name="John Doe", email="hello@example.com", role="student"
        )
        user.set_password("password")
        db.session.add(user)
        db.session.commit()

    yield app

    with app.app_context():
        User.query.delete()
        db.session.commit()


def test_get_user(client, setup):
    client.post("/api/auth/login", json={"username": "123", "password": "password"})

    response = client.get("/api/auth/user")
    assert response.json == {
        "email": "hello@example.com",
        "name": "John Doe",
        "user_id": "123",
        "class_ids": [],
    }
    assert response.status_code == 200


def test_get_user_unauthorised(client, setup):
    response = client.get("/api/auth/user")

    assert response.status_code == 401
