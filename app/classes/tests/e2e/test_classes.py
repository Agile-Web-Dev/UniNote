import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app import db
from app.libs.tests.fixtures import driver, server, wait
from app.models import Class, User


@pytest.fixture
def setup(server):
    with server.app_context():
        Class.query.delete()
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

        user.set_password("password")
        db.session.add_all(classes)
        db.session.add(user)
        db.session.commit()

    yield server

    with server.app_context():
        Class.query.delete()
        User.query.delete()

        db.session.commit()


def test_classes_enter(driver: webdriver.Chrome, wait, setup):
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

    class_cells = driver.find_elements(By.CLASS_NAME, "class-cell")

    assert len(class_cells) == 2

    assert EC.text_to_be_present_in_element(class_cells[0], "Test Class")
    assert EC.text_to_be_present_in_element(class_cells[1], "Test Class 2")

    class_cells[0].click()

    wait.until(EC.title_contains("Chatroom"))
    assert EC.url_contains(f"{base_url}/TEST123/chatroom")

    assert EC.text_to_be_present_in_element((By.ID, "chat-container"), "Hello World!")
