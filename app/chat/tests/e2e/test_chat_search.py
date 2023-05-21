import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from app import db
from app.libs.tests.fixtures import driver, server, wait
from app.models import Class, Message, User


@pytest.fixture
def setup(server):
    with server.app_context():
        Class.query.delete()
        Message.query.delete()
        User.query.delete()

        classes = [
            Class(name="Test Class", class_id="TEST123"),
            Class(name="Test Class 2", class_id="TEST456"),
        ]

        user = User(
            user_id="123",
            name="Jane Doe",
            email="hello@example.com",
            role="student",
            # class_ids=classes, # add this when classes are filtered by user
        )

        messages = [
            Message(created_by="Dan", class_id="TEST123", content="hey wassup guys"),
            Message(created_by="Bob", class_id="TEST123", content="Hai"),
            Message(created_by="John", class_id="TEST456", content="Sup"),
        ]

        user.set_password("password")
        db.session.add_all(classes)
        db.session.add_all(messages)
        db.session.add(user)
        db.session.commit()

    yield server

    with server.app_context():
        Class.query.delete()
        Message.query.delete()
        User.query.delete()
        db.session.commit()


def test_chat_search(driver: webdriver.Chrome, wait, setup):
    base_url = setup.config["E2E_URL"]
    driver.get(f"{base_url}/login")

    username = driver.find_element(By.ID, "username")
    username.send_keys("123")

    password = driver.find_element(By.ID, "password")
    password.send_keys("password")

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    wait.until(EC.title_contains("Dashboard"))

    assert driver.get_cookie("session") is not None

    driver.get(f"{base_url}/TEST123/chatroom")

    wait.until(EC.title_contains("Chatroom"))

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message")))

    search = driver.find_element(By.ID, "search-chat-input")

    search.send_keys("wassup")
    search.send_keys(Keys.RETURN)

    time.sleep(0.5)

    messages = driver.find_elements(By.CLASS_NAME, "message")

    assert len(messages) == 2

    assert "wassup" in messages[0].text

    assert (
        messages[0]
        .find_element(By.CLASS_NAME, "message-item")
        .value_of_css_property("background-color")
        == "rgba(89, 98, 108, 1)"
    )

    assert (
        messages[1]
        .find_element(By.CLASS_NAME, "message-item")
        .value_of_css_property("background-color")
        == "rgba(0, 0, 0, 0)"
    )

    wait.until(EC.title_contains("Chat"))
