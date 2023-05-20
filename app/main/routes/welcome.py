from flask import render_template

from . import bp


@bp.route("/welcome")
def welcome():
    return render_template("homepage.html", title="Welcome")
