from flask import redirect, render_template, url_for
from flask_login import current_user

from . import bp


@bp.route("/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("login.html", title="Login")
