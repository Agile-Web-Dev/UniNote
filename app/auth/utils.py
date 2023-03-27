import functools
from http import HTTPStatus

from flask import abort, redirect, request, url_for
from flask_login import current_user
from flask_socketio import disconnect

from app import login


@login.unauthorized_handler
def login_required():
    if request.blueprint == "main":
        return redirect(url_for("main.login"))
    abort(HTTPStatus.UNAUTHORIZED)


def login_required_socket(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped
