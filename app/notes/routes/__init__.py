from flask import Blueprint

bp = Blueprint("notes", __name__)

# needs to add the api file not the functions
from . import notes
