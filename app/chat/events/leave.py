from flask import session
from flask_socketio import emit, leave_room

from app import socketio
from app.auth.utils import login_required_socket


@socketio.on("leave", namespace="/chat")
def leave(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get("class_id")
    emit("status", {"msg": session.get("name") + " has left the room."}, room=room)
    leave_room(room)
