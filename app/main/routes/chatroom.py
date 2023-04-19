from flask import render_template, session
from flask_login import login_required
from app.models import Message

from app import db
from app.auth.utils import in_class
from app.models import load_user

from . import bp

from app.libs.processors import topbar
from app.libs.filters import format_datetime

@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
@in_class
def chatroom(class_id):
    session["class_id"] = class_id
    messages = Message.query.filter(Message.class_id == class_id)
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
        messages = messages
        # topbar_items=topbar_items
        # add chat messages here
    )
