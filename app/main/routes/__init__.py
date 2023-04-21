from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main.routes import chatroom, forum, login, notes, register
