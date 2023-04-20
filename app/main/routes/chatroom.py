from flask import render_template, session
from flask_login import login_required

from app import db
from app.auth.utils import in_class
from app.classes.routes.classes import get_class_info
from app.libs.filters import format_datetime
from app.libs.processors import topbar
from app.models import Message, load_user

from . import bp


@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
@in_class
def chatroom(class_id):
    session["class_id"] = class_id
    header_items = get_class_info(class_id)
    messages = Message.query.filter(Message.class_id == class_id)

    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
        header_items=header_items,
        messages=messages,
    )
