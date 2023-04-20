from flask import render_template
from flask_login import login_required

from . import bp


@bp.route("/<class_id>/notes", methods=["GET"])
@login_required
def notes(class_id):
    return render_template(
        "notes.html",
        title="Note Forum",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
