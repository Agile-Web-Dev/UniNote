from flask import make_response
from flask_login import login_required, logout_user

from . import bp


@login_required
@bp.route("/logout", methods=["GET"])
def logout():
    """
    Logs out a user.
    Endpoint: /api/auth/logout

    returns a header to remove the session cookie
    """
    logout_user()
    return make_response({"msg": "Logout successful"}, 200)
