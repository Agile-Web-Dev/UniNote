from flask import render_template
from flask_login import login_required

from app.models import load_user, Class
from app import db
from . import bp


@bp.route("/", methods=["GET"])
@bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    user = load_user()
    # get classes that the user is not in
    enrolled_classes = [u.class_id for u in user.class_ids]
    unenrolled_classes = Class.query.filter(~Class.class_id.in_(enrolled_classes)).all()
    print(unenrolled_classes)
    return render_template(
        "dashboard.html", title="Dashboard", enrolled_classes=user.class_ids, unenrolled_classes=unenrolled_classes
    )
