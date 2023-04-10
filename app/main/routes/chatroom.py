from flask import render_template, session
from flask_login import login_required

from . import bp


@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
def chatroom(class_id):
    session["class_id"] = class_id
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
