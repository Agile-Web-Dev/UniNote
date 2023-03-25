from flask import render_template

from . import bp


@bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html", title="Login")
