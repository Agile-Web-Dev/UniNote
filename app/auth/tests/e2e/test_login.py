from flask import url_for
import pytest

from app import db
from app.libs.tests.fixtures import app, server, driver
from app.models import User
from selenium import webdriver

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


def test_login_user_id(driver: webdriver.Chrome, setup):
    driver.get("http://localhost:3000")
    pass