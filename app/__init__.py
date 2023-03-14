from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.api.routes import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    from app.main.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
