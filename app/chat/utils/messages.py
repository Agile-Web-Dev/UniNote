
from app.models import Message
from app import db


from . import bp
@bp.route("/<class_id>", methods=["GET"])
def get_messages(class_id):
    '''get messages based on the current class'''
    msgsArr = []
    msgs = db.session.query(Message).filter(Message.class_id == class_id)
    for entry in msgs:
        msgsArr.append(entry.serialize())
    return msgsArr

