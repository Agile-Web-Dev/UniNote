from . import Base


class Ping(Base):
    def executor(room, args):
        return "pong!"
