class Base:
    commands = {}

    def __init_subclass__(self):
        self.commands[self.__name__.lower()] = self.executor
