import threading

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    with app.app_context():
        yield app


# * these fixtures cannot be scoped for socketio to work
@pytest.fixture()
def server():
    app = create_app()
    # * this must be disabled for the server to emit socket events
    # app.config.update({"TESTING": False})
    t = threading.Thread(target=app.run, kwargs={"port": "5000", "use_reloader": False})
    t.daemon = True
    t.start()

    with app.app_context():
        yield app


@pytest.fixture()
def driver(server):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    with webdriver.Chrome(options=chrome_options) as driver:
        yield driver


@pytest.fixture()
def wait(driver):
    yield WebDriverWait(driver, 5)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
