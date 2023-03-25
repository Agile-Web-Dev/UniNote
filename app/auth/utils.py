from http import HTTPStatus
from flask import abort, redirect, request, url_for
from app import login


@login.unauthorized_handler
def unauthorized():
    if request.blueprint == 'main':
        return redirect(url_for('main.login'))
    abort(HTTPStatus.UNAUTHORIZED)