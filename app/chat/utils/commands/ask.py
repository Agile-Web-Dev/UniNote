from ..openai import get_index
from . import Base


class Ask(Base):
    def executor(room, args):
        if args == "":
            return "Please provide a question."

        index = get_index(room)
        query = str(index.query(args)).strip()
        return query
