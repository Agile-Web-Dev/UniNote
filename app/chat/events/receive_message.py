from flask import session
from flask_login import current_user
from flask_socketio import emit
from app.chat.utils import command_handler

from app import socketio
from app.auth.utils import login_required_socket


@socketio.on("receive_message", namespace="/chat")
@login_required_socket
def receive_message(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get("class_id")
    
    emit(
        "receiveMessage",
        {"name": current_user.name, "msg": message["msg"], "isBot": False},
        room=room,
        broadcast=True,
    )

    if message["intent"] == "command":
        msg = command_handler(message["msg"], room)
        emit(
            "receiveMessage",
            {"name": "UniNote Bot", "msg": msg, "isBot": True},
            room=room,
            broadcast=True,)
