from flask import render_template
from flask_login import login_required

from app.classes.routes.links import get_class_links
from app.main.utils import get_default_links

from . import bp


@bp.route("/<class_id>/notes", methods=["GET"])
@login_required
def notes(class_id):
    """
    renders notes template
    endpoint: /class/<class_id>/notes
    """
    nav_items = get_default_links(class_id) + get_class_links(class_id)

    return render_template(
        "notes.html",
        title="Note Forum",
        nav_items=nav_items,
    )
