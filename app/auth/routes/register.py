import re

from flask import make_response, request
from flask_login import login_user

from app import db
from app.models import User

from . import bp


@bp.route("/register", methods=["POST"])
def register():
    """
    Register a new student.
    Endpoint: /api/auth/register
    POST JSON data:
    - userId
    - email
    - password
    - name
    """
    data = request.get_json()
    user_id = data.get("userId", "")
    email = data.get("email", "")
    password = data.get("password", "")
    name = data.get("name", "")

    if user_id == "" or email == "" or password == "" or name == "":
        return make_response({"msg": "Missing fields"}, 400)

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        return make_response({"msg": "Invalid email"}, 400)

    if len(password) < 8:
        return make_response({"msg": "Password must be at least 8 characters"}, 400)

    user = User.query.filter((User.user_id == user_id) | (User.email == email)).first()
    if user is not None:
        return make_response({"msg": "User already exists"}, 400)

    user = User(user_id=user_id, email=email, name=name, role="student")
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    return make_response({"msg": "Registration successful"}, 201)
