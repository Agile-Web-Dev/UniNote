from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main.routes import dashboard

from app.main.routes import login

from app.main.routes import chatroom

from app.main.routes import notes
