from app import db
from app.models import Message

from . import bp


@bp.route("/<class_id>", methods=["GET"])
def get_messages(class_id):
    """
    get messages based on the current class
    endpoint: /api/class/<class_id>/messages
    serializes messages into json
    """
    msg_arr = []
    msgs = db.session.query(Message).filter(Message.class_id == class_id)
    for entry in msgs:
        msg_arr.append(entry.serialize())
    return msg_arr
