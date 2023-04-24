from .commands import *

def command_handler(command, room):
    command = command[1:].lower()
    
    if command in Base.commands:
        return Base.commands[command](room)

    return "Command not found"