from flask import render_template
from flask_login import login_required

from app.classes.routes.links import get_class_links

from . import bp


@bp.route("/<class_id>/notes", methods=["GET"])
@login_required
def notes(class_id):
    nav_items = [
        {
            "name": "Chat",
            "icon": "bi-chat-left-dots-fill",
            "url": f"/{class_id}/chatroom",
        },
        {"name": "Notes", "icon": "bi-pencil-square", "url": f"/{class_id}/notes"},
    ] + get_class_links(class_id)

    return render_template(
        "notes.html",
        title="Note Forum",
        nav_items=nav_items,
    )
