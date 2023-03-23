from flask import render_template

from . import bp


@bp.route("/dashboard", methods=["GET"])
def home():
    return render_template("dashboard.html", title="Dashboard")
