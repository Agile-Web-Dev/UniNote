from flask import session
from flask_login import current_user
from flask_socketio import emit

from app import socketio,db
from app.models import Message
from app.auth.utils import login_required_socket


@socketio.on("receive_message", namespace="/chat")
@login_required_socket
def receive_message(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get("room")
    emit(
        "receiveMessage",
        {"msg": current_user.name + ": " + message["msg"]},
        room=room,
        broadcast=True,
    )
    msg = Message(created_by = current_user.name, class_id = room, content = message)
    db.session.add(msg)
    db.session.commit()


