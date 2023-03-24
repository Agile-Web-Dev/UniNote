from flask import render_template

from . import bp


@bp.route("/chatroom", methods=["GET"])
def chatroom():
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
