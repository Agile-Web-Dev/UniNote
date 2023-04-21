from flask import render_template

from . import bp


@bp.route("/<class_id>/notes", methods=["GET"])
def notes(class_id):
    return render_template(
        "notes.html",
        title="Note Forum",
        nav_items=["Chat", "Notes", "Labs", "Project", "Exam"],
    )
