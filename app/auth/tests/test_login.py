import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import User


@pytest.fixture
def setup(app):
    print("Setting up...")
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


def test_login_user_id(client, setup):
    response = client.post(
        "/api/auth/login", json={"username": "123", "password": "password"}
    )
    print(response.text)
    assert response.status_code == 200


def test_login_email(client, setup):
    response = client.post(
        "/api/auth/login",
        json={"username": "hello@example.com", "password": "password"},
    )
    print(response.text)
    assert response.status_code == 200


def test_login_username_fail(client, setup):
    response = client.post(
        "/api/auth/login", json={"username": "1234", "password": "password"}
    )
    print(response.text)
    assert response.status_code == 401


def test_login_password_fail(client, setup):
    response = client.post(
        "/api/auth/login", json={"username": "123", "password": "password1"}
    )
    print(response.text)
    assert response.status_code == 401


def test_login_empty(client, setup):
    response = client.post("/api/auth/login", json={"username": "", "password": ""})
    print(response.text)
    assert response.status_code == 400
