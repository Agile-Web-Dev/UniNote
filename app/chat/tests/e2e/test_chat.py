import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app import db
from app.libs.tests.fixtures import app, driver, server, wait
from app.libs.tests.helpers import login_as
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


def test_chat_message_send(driver: webdriver.Chrome, wait, setup):
    base_url = f"{setup.config['E2E_URL']}"

    login_as(driver, base_url, {"user_id": "123", "password": "password"})

    driver.get(f"{base_url}/chat")

    wait.until(EC.title_contains("Chatroom"))

    assert driver.get_cookie("session") is not None

    chatbox = driver.find_element(By.ID, "chatbox")
    send_button = driver.find_element(By.ID, "send-button")

    chatbox.send_keys("Hello World!")
    send_button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "chatbox"), ""))

    assert EC.text_to_be_present_in_element((By.ID, "chat-container"), "Hello World!")

    driver.refresh()

    wait.until(EC.title_contains("Chat"))

    assert EC.text_to_be_present_in_element((By.ID, "chat-container"), "Hello World!")
