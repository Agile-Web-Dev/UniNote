from flask import session
from flask_login import current_user
from flask_socketio import emit

from app import db, socketio
from app.auth.utils import login_required_socket
from app.chat.utils import command_handler
from app.models import Message


@socketio.on("receive_message", namespace="/chat")
@login_required_socket
def receive_message(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""

    room = session.get("class_id")
    msg = Message(
        created_by=current_user.name, class_id=room, content=message.get("msg")
    )
    db.session.add(msg)
    db.session.commit()

    emit(
        "receiveMessage",
        msg.serialize(),
        room=room,
        broadcast=True,
    )

    if message["intent"] == "command":
        bot_res = command_handler(message["msg"], room)

        msg = Message(created_by="UniNote Bot", class_id=room, content=bot_res)
        db.session.add(msg)
        db.session.commit()
        serialised_message = msg.serialize()
        serialised_message["isBot"] = True
        emit(
            "receiveMessage",
            serialised_message,
            room=room,
            broadcast=True,
        )
