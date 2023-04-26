from flask import render_template, session
from flask_login import login_required

from app import db
from app.auth.utils import in_class
from app.classes.routes.classes import get_class_info

from . import bp


@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
@in_class
def chatroom(class_id):
    header_items = get_class_info(class_id)
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
        header_items=header_items,
    )
