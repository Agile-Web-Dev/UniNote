from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "main.login"
socketio = SocketIO()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    socketio.init_app(app)

    from app.api.routes import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    from app.auth.routes import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from app.notes.routes import bp as notes_bp

    app.register_blueprint(notes_bp, url_prefix="/api/notes")

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app

import app.chat.events
from app import models
