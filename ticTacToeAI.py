from random import randint


class TicTacToe:
    
    def __init__(self):
        self.board = None
        self.current_mark = None
        self.player1 = None
        self.player2 = None
        self.MODES = {"user", "easy", "medium", "hard", "exit"}

    @staticmethod
    def available_moves(pos):
        moves = []
        for i in range(3):
            for j in range(3):
                if pos[i][j] == ' ':
                    moves.append((i, j))

        return moves

    @staticmethod
    def check(pos):
        WIN_POS = {('X', 'X', 'X'), ('O', 'O', 'O')}
        for i in range(3):
            if (pos[i][0], pos[i][1], pos[i][2]) in WIN_POS:
                return pos[i][0]

            if (pos[0][i], pos[1][i], pos[2][i]) in WIN_POS:
                return pos[0][i]

        if (pos[0][0], pos[1][1], pos[2][2]) in WIN_POS or \
           (pos[0][2], pos[1][1], pos[2][0]) in WIN_POS:
            return pos[1][1]

        if all([pos[i][j] != ' ' for i in range(3) for j in range(3)]):
            return "Draw"

    def print_board(self):
        print("-" * 9)
        for i in range(3):
            print("| " + " ".join(self.board[i]) + " |")
        print("-" * 9)

    def get_commands(self):
        while True:
            try:
                commands = input("Input command: ").lower().split()
                if commands == ["exit"]:
                    quit()
                else:
                    assert len(commands) == 3 and commands[0] == "start"
                    assert commands[1] in self.MODES
                    assert commands[2] in self.MODES

                    self.player1 = commands[1]
                    self.player2 = commands[2]
                    return
            except AssertionError:
                print("Bad parameters!")
                continue

    def user_move(self):
        while True:
            try:
                coord = input("Enter the coordinates: ").split()
                assert len(coord) == 2
                user_move = (int(coord[0]) - 1, int(coord[1]) - 1)
                assert 0 <= user_move[0] <= 2 and 0 <= user_move[1] <= 2
            except (ValueError, AssertionError):
                print("Coordinates should be from 1 to 3!")
                continue

            if self.board[user_move[0]][user_move[1]] == ' ':
                self.board[user_move[0]][user_move[1]] = self.current_mark
                return
            else:
                print("This cell is occupied! Choose another one!")
                continue

    def random_move(self):
        random_move = (randint(0, 2), randint(0, 2))
        available_moves = self.available_moves(self.board)
        while random_move not in available_moves:
            random_move = (randint(0, 2), randint(0, 2))

        self.board[random_move[0]][random_move[1]] = self.current_mark

    def easy_move(self):
        print("Making move level \"easy\"")
        self.random_move()

    def medium_move(self):
        print("Making move level \"medium\"")
        medium_move = None
        available_moves = self.available_moves(self.board)

        for move in available_moves:
            self.board[move[0]][move[1]] = self.current_mark
            if self.check(self.board) == self.current_mark:
                medium_move = (move[0], move[1])
            self.board[move[0]][move[1]] = ' '

        for move in available_moves:
            self.board[move[0]][move[1]] = "O" if self.current_mark == "X" else "X"
            if self.check(self.board) == ("O" if self.current_mark == "X" else "X"):
                medium_move = (move[0], move[1])
            self.board[move[0]][move[1]] = ' '

        if medium_move is not None:
            self.board[medium_move[0]][medium_move[1]] = self.current_mark
        else:
            self.random_move()

    def evaluate(self, pos):
        result = self.check(pos)

        if result == self.current_mark:
            return 1
        elif result == ("X" if self.current_mark == "O" else "O"):
            return -1
        elif result == "Draw":
            return 0

    def minimax(self, position, alpha, beta, is_maximizing):
        score = self.evaluate(position)
        if score is not None:
            return score

        moves = self.available_moves(position)
        if is_maximizing:
            value = -2
            for move in moves:
                position[move[0]][move[1]] = self.current_mark
                value = max(value, self.minimax(position, alpha, beta, False))
                position[move[0]][move[1]] = ' '
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = 2
            for move in moves:
                position[move[0]][move[1]] = "X" if self.current_mark == "O" else "O"
                value = min(value, self.minimax(position, alpha, beta, True))
                position[move[0]][move[1]] = ' '
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def hard_move(self):
        print("Making move level \"hard\"")
        hard_move = None
        best_eval = -2

        for move in self.available_moves(self.board):
            self.board[move[0]][move[1]] = self.current_mark
            move_eval = self.minimax(self.board, -2, 2, False)
            self.board[move[0]][move[1]] = ' '

            if move_eval > best_eval:
                best_eval = move_eval
                hard_move = (move[0], move[1])

        self.board[hard_move[0]][hard_move[1]] = self.current_mark

    def make_move(self, player):
        match player:
            case "user":
                self.user_move()
            case "easy":
                self.easy_move()
            case "medium":
                self.medium_move()
            case "hard":
                self.hard_move()

    def loop(self):
        while True:
            self.get_commands()
            self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.current_mark = "X"
            self.print_board()

            while True:
                self.make_move(self.player1)
                self.print_board()
                winner = self.check(self.board)
                if winner is not None:
                    print("X wins" if winner != "Draw" else "Draw")
                    break
                self.current_mark = "O"

                self.make_move(self.player2)
                self.print_board()
                winner = self.check(self.board)
                if winner is not None:
                    print("O wins" if winner != "Draw" else "Draw")
                    break
                self.current_mark = "X"


if __name__ == "__main__":
    game = TicTacToe()
    game.loop()
