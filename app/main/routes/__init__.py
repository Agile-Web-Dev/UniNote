from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main.routes import chatroom, dashboard, login, notes, register, welcome
