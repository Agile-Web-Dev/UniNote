import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

        notes = [
            Note(
                created_by="123",
                class_id="TEST123",
                title="My Mom",
                content="Test content 0",
            ),
            Note(
                created_by="123",
                class_id="TEST123",
                title="Random thoughts",
                content="Test content",
            ),
            Note(
                created_by="123",
                class_id="TEST456",
                title="asdsag",
                content="What is this?",
            ),
        ]

        user.set_password("password")
        db.session.add_all(classes)
        db.session.add_all(notes)
        db.session.add(user)
        db.session.commit()

    yield server

    with server.app_context():
        Class.query.delete()
        Note.query.delete()
        User.query.delete()
        db.session.commit()


def test_search_notes(driver: webdriver.Chrome, wait, setup):
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
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "note-item")))

    note_items = driver.find_elements(By.CLASS_NAME, "note-item")

    assert len(note_items) == 2

    searchbar = driver.find_element(By.ID, "notes-searchbar")

    searchbar.send_keys("mom")
    searchbar.send_keys(Keys.ENTER)

    time.sleep(0.5)

    new_note_items = driver.find_elements(By.CLASS_NAME, "note-item")

    assert len(new_note_items) == 1
