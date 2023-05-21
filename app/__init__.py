from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
socketio = SocketIO()


def create_app(config_class=Config, socketio_async_mode=None):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.app_context().push()

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    socketio.init_app(app, async_mode=socketio_async_mode)

    from app.api.routes import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    from app.auth.routes import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from app.notes.routes import bp as notes_bp

    app.register_blueprint(notes_bp, url_prefix="/api/notes")

    from app.classes.routes import bp as classes_bp

    app.register_blueprint(classes_bp, url_prefix="/api/classes")

    from app.chat.routes import bp as messages_bp

    app.register_blueprint(messages_bp, url_prefix="/api/messages")

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app


import app.chat.events
from app import models
