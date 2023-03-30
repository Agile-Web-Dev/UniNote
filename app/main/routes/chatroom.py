from flask import render_template
from flask_login import login_required

from . import bp


@bp.route("/chatroom", methods=["GET"])
@login_required
def chatroom():
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
