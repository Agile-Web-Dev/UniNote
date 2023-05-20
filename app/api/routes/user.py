from flask import make_response, request
from flask_login import login_required

from app.models import Class, load_user
from app import db
from . import bp


@bp.route("/user", methods=["GET"])
@login_required
def user():
    """
    Returns the current user.
    Endpoint: /api/user
    """
    user = load_user()
    if user is None:
        return make_response({"msg": "User not found"}, 404)
    return make_response(user.serialize(), 200)

@bp.route("/user/class", methods=["GET"])
@login_required
def get_classes():
    """
    Returns the current user's classes.
    Endpoint: /api/user/class
    """
    user = load_user()
    if user is None:
        return make_response({"msg": "User not found"}, 404)
    return make_response({"classes": [c.serialize() for c in user.class_ids]}, 200)

@bp.route("/user/class", methods=["POST"])
@login_required
def add_class():
    """
    Add a new class to the user's list of classes.
    Endpoint: /api/user/class
    """

    data = request.get_json()
    class_id = data.get("classId", "")

    user = load_user()
    if user is None:
        return make_response({"msg": "User not found"}, 404)

    if class_id in user.class_ids:
        return make_response({"msg": "Class already added"}, 400)

    class_id_object = Class.query.filter_by(class_id=class_id).first()
    user.class_ids.append(class_id_object)
    db.session.commit()
    return make_response(user.serialize(), 200)
