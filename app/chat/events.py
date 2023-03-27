from flask import session
from flask_login import current_user
from flask_socketio import emit, join_room, leave_room

from app import socketio
from app.auth.utils import login_required_socket


@socketio.on("joined", namespace="/chat")
@login_required_socket
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get("room")
    join_room(room)
    
    emit("joined", {"msg": current_user.name + " has entered the room."}, room=room, broadcast=True)



@socketio.on("receive_message", namespace="/chat")
@login_required_socket
def receive_message(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get("room")
    emit("receiveMessage", {"msg": current_user.name + ": " + message["msg"]}, room=room, broadcast=True)

# @socketio.on("leave", namespace="/chat")
# def left(message):
#     """Sent by clients when they leave a room.
#     A status message is broadcast to all people in the room."""
#     room = session.get("room")
#     leave_room(room)
#     emit("status", {"msg": session.get("name") + " has left the room."}, room=room)
