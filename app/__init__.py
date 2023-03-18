from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config

login_manager = LoginManager()
db = SQLAlchemy()
socketio = SocketIO()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    from app.api.routes import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app


from app import models
