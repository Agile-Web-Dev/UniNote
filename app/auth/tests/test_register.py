import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import User


@pytest.fixture
def setup(app):
    with app.app_context():
        User.query.delete()
        db.session.commit()

    yield app

    with app.app_context():
        User.query.delete()
        db.session.commit()


def test_register(client, setup):
    data = {
        "student_id": "123",
        "name": "John Doe",
        "email": "hello@example.com",
        "password": "password",
    }
    response = client.post("/api/auth/register", json=data)

    assert response.status_code == 201


def test_missing_fields(client, setup):
    data = {"student_id": "123", "name": "John Doe", "password": "password"}
    response = client.post("/api/auth/register", json=data)

    assert response.status_code == 400


def test_duplicate(client, setup):
    data = {
        "student_id": "123",
        "name": "John Doe",
        "email": "hello@example.com",
        "password": "password",
    }
    response = client.post("/api/auth/register", json=data)
    response = client.post("/api/auth/register", json=data)

    assert response.status_code == 400
