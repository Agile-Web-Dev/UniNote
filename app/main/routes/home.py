from flask import render_template

from . import bp


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def home():
    return render_template("index.html", title="Home")
