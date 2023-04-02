import threading
from app import socketio
import pytest
from selenium import webdriver
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    with app.app_context():
        yield app
        
@pytest.fixture(scope="session")
def server():
    app = create_app()
    app.config.update({"TESTING": True})
    t = threading.Thread(target=app.run, kwargs={"port":"3000", "use_reloader": False})
    t.daemon = True
    t.start()

@pytest.fixture(scope="session")
def driver(server):
    with webdriver.Chrome() as driver:
        yield driver
        

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
