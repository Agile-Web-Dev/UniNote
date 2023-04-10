from flask import render_template
from flask_login import login_required
from app.models import User, load_user

from . import bp


@bp.route("/", methods=["GET"])
@bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    user = load_user()
    return render_template(
        "dashboard.html",
        title="Dashboard",
        class_ids=user.class_ids
    )
