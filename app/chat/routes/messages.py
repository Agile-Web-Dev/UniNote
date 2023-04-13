
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

@bp.route("/", methods=["POST"])
def post_messages(message_id, created_by,class_id,content):
    '''post messages based on the current window'''
    message = Message(message_id = message_id,created_by = created_by, class_id = class_id, content = content)
    db.session.add(message)
    db.session.commit()
    return message