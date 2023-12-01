class Command:
    def __init__(self, command_operation: str, command_argument=None):
        self.command_operation = command_operation
        self.command_argument = command_argument
