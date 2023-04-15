from flask import make_response
from flask_login import login_required

from app.models import load_user

from app.auth.routes import bp


@bp.route("/user", methods=["GET"])
@login_required
def get_user():
    """
    Returns the current user.
    Endpoint: /api/user
    """
    user = load_user()
    if user is None:
        return make_response({"msg": "User not found"}, 404)
    return make_response(user.serialize(), 200)
