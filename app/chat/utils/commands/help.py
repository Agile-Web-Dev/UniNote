from . import Base


class Help(Base):
    def executor(room, args):
        commands = ", ".join(Base.commands.keys())
        return f"Available commands: {commands}"
