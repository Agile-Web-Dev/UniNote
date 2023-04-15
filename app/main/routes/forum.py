from flask import render_template

from . import bp


@bp.route("/<class_id>/notes", methods=["GET"])
def forum():
    return render_template(
        "forum.html",
        title="Note Forum",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
