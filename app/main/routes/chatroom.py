from flask import render_template, session
from flask_login import login_required

from app import db
from app.auth.utils import in_class
from app.models import load_user

from . import bp, topbar


@bp.route("/<class_id>/chatroom", methods=["GET"])
@login_required
@in_class
def chatroom(class_id):
    session["class_id"] = class_id
    # user = load_user()
    # topbar_items = user.class_ids
    return render_template(
        "chatroom.html",
        title="Chatroom",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
        # topbar_items=topbar_items
        # add chat messages here
    )
