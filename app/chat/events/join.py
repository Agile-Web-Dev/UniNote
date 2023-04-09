from flask import session
from flask_login import current_user
from flask_socketio import emit, join_room

from app import socketio
from app.auth.utils import login_required_socket


@socketio.on("join", namespace="/chat")
@login_required_socket
def join(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get("room")
    join_room(room)

    emit(
        "join",
        {"msg": current_user.name + " has entered the room."},
        room=room,
        broadcast=True,
    )
