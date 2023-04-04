from flask import Blueprint

bp = Blueprint("classes", __name__)

#needs to add the api file not the functions
from . import classes
