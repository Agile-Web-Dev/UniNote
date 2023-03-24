from flask import render_template

from . import bp


@bp.route("/forum", methods=["GET"])
def forum():
    return render_template("forum.html", title="Note Forum")
