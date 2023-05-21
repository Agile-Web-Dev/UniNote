import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app import db
from app.libs.tests.fixtures import driver, server, wait
from app.models import Class, Note, User


@pytest.fixture
def setup(server):
    with server.app_context():
        Class.query.delete()
        Note.query.delete()
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
        Note.query.delete()
        User.query.delete()
        db.session.commit()


def test_add_note_from_chat(driver: webdriver.Chrome, wait, setup):
    base_url = setup.config["E2E_URL"]
    driver.set_window_size(1920, 1080)
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

    assert driver.find_element(By.ID, "note-bar") is not None

    note_header = driver.find_element(By.ID, "note-header")
    note_content = driver.find_element(By.ID, "note-content")

    assert note_header is not None
    assert note_content is not None

    note_header.send_keys("Test Note")
    note_content.send_keys("Test Note Content")

    send_button = driver.find_element(By.ID, "note-share-button")

    assert send_button is not None

    wait.until(
        EC.text_to_be_present_in_element_value(
            (By.ID, "note-content"), "Test Note Content"
        )
    )

    time.sleep(0.5)  # selenium will not wait properly

    send_button.click()

    wait.until(EC.element_to_be_clickable((By.ID, "note-share-button")))

    driver.get(f"{base_url}/TEST123/notes")

    wait.until(EC.title_contains("Note Forum"))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "note-item")))

    assert len(driver.find_elements(By.CLASS_NAME, "note-item")) == 1


def test_add_note_from_notes(driver: webdriver.Chrome, wait, setup):
    base_url = setup.config["E2E_URL"]
    driver.set_window_size(1920, 1080)
    driver.get(f"{base_url}/login")

    username = driver.find_element(By.ID, "username")
    username.send_keys("123")

    password = driver.find_element(By.ID, "password")
    password.send_keys("password")

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    wait.until(EC.title_contains("Dashboard"))

    assert driver.get_cookie("session") is not None

    driver.get(f"{base_url}/TEST123/notes")

    wait.until(EC.title_contains("Note Forum"))

    assert driver.find_element(By.ID, "note-bar") is not None

    note_header = driver.find_element(By.ID, "note-header")
    note_content = driver.find_element(By.ID, "note-content")

    assert note_header is not None
    assert note_content is not None

    note_header.send_keys("Test Note")
    note_content.send_keys("Test Note Content")

    send_button = driver.find_element(By.ID, "note-share-button")

    assert send_button is not None

    wait.until(
        EC.text_to_be_present_in_element_value(
            (By.ID, "note-content"), "Test Note Content"
        )
    )

    time.sleep(0.5)  # selenium will not wait properly

    send_button.click()

    wait.until(EC.element_to_be_clickable((By.ID, "note-share-button")))

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "note-item")))

    assert len(driver.find_elements(By.CLASS_NAME, "note-item")) == 1
