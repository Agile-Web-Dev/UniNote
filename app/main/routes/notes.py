from flask import render_template

from . import bp


@bp.route("/notes", methods=["GET"])
def home():
    return render_template("notes.html", title="Notes")
