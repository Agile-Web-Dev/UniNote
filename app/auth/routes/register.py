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
    - student_id
    - email
    - password
    - name
    """
    data = request.get_json()
    student_id = data.get("student_id", "")
    email = data.get("email", "")
    password = data.get("password", "")
    name = data.get("name", "")

    if student_id == "" or email == "" or password == "" or name == "":
        return make_response({"msg": "Missing fields"}, 400)

    user = User.query.filter(
        (User.user_id == student_id) | (User.email == email)
    ).first()
    if user is not None:
        return make_response({"msg": "User already exists"}, 400)

    user = User(user_id=student_id, email=email, name=name, role="student")
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    return make_response({"msg": "Registration successful"}, 201)
