from flask import Blueprint

bp = Blueprint("classes", __name__)

from . import classes
