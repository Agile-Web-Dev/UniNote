from flask import Blueprint

bp = Blueprint("notes", __name__)

from . import getNotes,postNotes
