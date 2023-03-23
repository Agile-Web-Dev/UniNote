from flask import render_template

from . import bp


@bp.route("/chatroom", methods=["GET"])
def home():
    return render_template("chatroom.html", title="Chatroom")
