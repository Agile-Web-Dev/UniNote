from flask import render_template
from flask_login import login_required

from . import bp


@bp.route("/", methods=["GET"])
@bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard")
