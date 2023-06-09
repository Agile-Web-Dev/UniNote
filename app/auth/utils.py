import functools
from http import HTTPStatus

from flask import abort, redirect, request, session, url_for
from flask_login import current_user
from flask_socketio import disconnect

from app import login


@login.unauthorized_handler
def login_required():
    """
    redirect to welcome page if user is not authenticated
    """
    if request.blueprint == "main":
        return redirect(url_for("main.welcome"))
    abort(HTTPStatus.UNAUTHORIZED)


def login_required_socket(f):
    """
    disconnect socket if user is not authenticated
    """

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        return f(*args, **kwargs)

    return wrapped


def in_class(f):
    """
    check if user is in class
    """

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        cids = [cid.class_id for cid in current_user.class_ids]
        if kwargs["class_id"] not in cids:
            abort(HTTPStatus.UNAUTHORIZED)

        session["class_id"] = kwargs.get("class_id")
        return f(*args, **kwargs)

    return wrapped
