from flask import redirect, render_template, url_for
from flask_login import current_user

from . import bp


@bp.route("/register", methods=["GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("register.html", title="Register")
