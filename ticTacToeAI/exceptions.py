
class InvalidCommandError(Exception):
    def __init__(self, command: str):
        self.message = f"Invalid command: '{command}'"
        super().__init__(self.message)


class InvalidModeError(Exception):
    def __init__(self, mode: str):
        self.message = f"Invalid mode: '{mode}'"
        super().__init__(self.message)


class OccupiedCellException(Exception):
    def __init__(self, move: tuple):
        self.message = f"The cell ({move[0]}, {move[1]}) is occupied."
        super().__init__(self.message)
