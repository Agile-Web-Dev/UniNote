from flask import make_response, request
from flask_login import login_user, current_user

from app.models import User
from . import bp


@bp.route('/login', methods=['POST'])
def login():
    '''
    Logs in a user.
    Endpoint: /api/auth/login
    POST JSON data:
    - user: can be either user_id or email
    - password
    
    returns a header to set a session cookie
    '''
    username = request.get_json().get("username", "")
    password = request.get_json().get("password", "")
    if username == "" or password == "":
        return make_response({"msg": "Missing username or password"}, 400)

    if current_user.is_authenticated: # type: ignore
        return make_response({"msg": "Already logged in"}, 200)

    user = User.query.filter((User.user_id==username) | (User.password==username)).first()
    if user is None or not user.check_password(password):
        return make_response({"msg": "Invalid username or password"}, 401)

    if login_user(user):
        print(user)
    return make_response({"msg": "Logged in"}, 200)