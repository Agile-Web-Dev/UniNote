import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app import db
from app.libs.tests.fixtures import app, driver, server, wait
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


def test_login_user_id(driver: webdriver.Chrome, wait, setup):
    base_url = setup.config["E2E_URL"]
    driver.get(base_url)

    username = driver.find_element(By.ID, "username")
    username.send_keys("123")

    password = driver.find_element(By.ID, "password")
    password.send_keys("password")

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    wait.until(EC.title_contains("Dashboard"))

    assert driver.get_cookie("session") is not None
