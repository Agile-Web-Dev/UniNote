from flask import make_response, request
from flask_login import current_user, login_required, login_user

from app import db
from app.models import User

from . import bp


@bp.route("/user", methods=["GET"])
@login_required
def get_user():
    """
    Returns the current user.
    Endpoint: /api/auth/user
    """
    user = User.query.filter(User.user_id == current_user.user_id).first()
    if user is None:
        return make_response({"msg": "User not found"}, 404)
    return make_response(user.serialize(), 200)
