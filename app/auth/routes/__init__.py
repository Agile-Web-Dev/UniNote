from flask import Blueprint

from ...api.routes import user

bp = Blueprint("auth", __name__)

from . import login, logout, register
