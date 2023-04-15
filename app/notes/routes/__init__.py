from flask import Blueprint

bp = Blueprint("notes", __name__)

from . import notes
