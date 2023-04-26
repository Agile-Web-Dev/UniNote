from .commands import *


def command_handler(msg, room):
    msg = msg[1:].lower().split(" ", 1)
    command = msg[0]
    if len(msg) != 1:
        args = msg[1]
    else:
        args = ""
    if command in Base.commands:
        return Base.commands[command](room, args)

    return "Command not found"
