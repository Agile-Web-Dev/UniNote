from flask import make_response, request
from flask_login import current_user, login_required, login_user

from app import db
from app.models import User

from . import bp

@login_required
@bp.route("/user", methods=["GET"])
def get_user():
    """
    Returns the current user.
    Endpoint: /api/auth/user
    """
    user = User.query.filter(User.user_id == current_user.user_id).first()
    if user is None:
        return make_response({"msg": "User not found"}, 404)
    return make_response(
        {"user_id": user.user_id, "email": user.email, "name": user.name}, 200
    )
