from flask import render_template, session
from flask_login import login_required

from app import db
from app.auth.utils import in_class
from app.classes.routes.classes import get_class_info
from app.libs.filters import format_datetime
from app.libs.processors import topbar
from app.models import Class, Message, load_user

from . import bp


@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
@in_class
def chatroom(class_id):
    session["class_id"] = class_id
    messages = Message.query.filter(Message.class_id == class_id)
    class_links = [
        {
            "name": x,
            "icon": "link",
            "url": x,
        }
        for x in get_class_info()["links"]
    ]

    nav_items = [
        {
            "name": "Chat",
            "icon": "bi-chat-left-dots-fill",
            "url": f"/{class_id}/chatroom",
        },
        {"name": "Notes", "icon": "bi-pencil-square", "url": f"/{class_id}/notes"},
    ] + class_links

    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=nav_items,
        messages=messages,
    )
