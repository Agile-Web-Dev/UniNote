from flask import render_template
from flask_login import login_required

from app.classes.routes.classes import get_class_users

from . import bp


@bp.route("/chatroom", methods=["GET"])
@bp.route("/chatroom/<class_id>", methods=["GET"])
@login_required
def chatroom(class_id):
    header_items = get_class_users(class_id)
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
        header_items=header_items
    )
