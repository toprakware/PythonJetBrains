import exceptions


class Board:

    game_board = None
    MODES = {"user", "easy", "medium", "hard", "exit"}

    @classmethod
    def print_board(cls):
        print("-" * 9)
        for i in range(3):
            print("| " + " ".join(cls.game_board[i]) + " |")
        print("-" * 9)

    @classmethod
    def make_move(cls, move: tuple[int, int], mark: str):
        cls.game_board[move[0]][move[1]] = mark

    @classmethod
    def unmake_move(cls, move: tuple[int, int]):
        cls.game_board[move[0]][move[1]] = ' '

    @classmethod
    def generate_moves(cls) -> list[tuple[int, int]]:
        moves = []
        for i in range(3):
            for j in range(3):
                if cls.game_board[i][j] == ' ':
                    moves.append((i, j))

        return moves

    @classmethod
    def check_game(cls) -> str:
        WIN_POS = {('X', 'X', 'X'), ('O', 'O', 'O')}
        for i in range(3):
            if (cls.game_board[i][0], cls.game_board[i][1], cls.game_board[i][2]) in WIN_POS:
                return cls.game_board[i][0]

            if (cls.game_board[0][i], cls.game_board[1][i], cls.game_board[2][i]) in WIN_POS:
                return cls.game_board[0][i]

        if (cls.game_board[0][0], cls.game_board[1][1], cls.game_board[2][2]) in WIN_POS or \
           (cls.game_board[0][2], cls.game_board[1][1], cls.game_board[2][0]) in WIN_POS:
            return cls.game_board[1][1]

        if all([cls.game_board[i][j] != ' ' for i in range(3) for j in range(3)]):
            return "Draw"

    @classmethod
    def evaluate(cls, mark: str) -> int:
        """
        Returns the evaluation of the terminal state
        """
        result = cls.check_game()
        opponent_mark = "O" if mark == "X" else "X"

        if result == mark:
            return 1
        elif result == opponent_mark:
            return -1
        elif result == "Draw":
            return 0

    @classmethod
    def get_commands(cls) -> tuple[str, str]:
        while True:
            try:
                commands = input("Input command: ").lower().split()
                if commands == ["exit"]:
                    quit()

                if commands[0] != "start":
                    raise exceptions.InvalidCommandError(commands[0])
                elif commands[1] not in cls.MODES:
                    raise exceptions.InvalidModeError(commands[1])
                elif commands[2] not in cls.MODES:
                    raise exceptions.InvalidModeError(commands[2])

                return commands[1], commands[2]
            except IndexError:
                print("Bad parameters!")
                continue
            except (exceptions.InvalidCommandError, exceptions.InvalidModeError) as e:
                print(e)
                continue
