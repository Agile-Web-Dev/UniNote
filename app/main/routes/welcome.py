from flask import render_template

from . import bp


@bp.route("/welcome", methods=["GET"])
def welcome():
    return render_template("welcome.html", title="Welcome")
