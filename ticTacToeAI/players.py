from random import choice

from board import Board
import exceptions


class HumanPlayer:

    @staticmethod
    def user_move(mark: str):
        while True:
            try:
                row = int(input("Enter the row: "))
                column = int(input("Enter the column: "))
                if Board.game_board[row - 1][column - 1] != ' ':
                    raise exceptions.OccupiedCellException((row, column))

                move = (row - 1, column - 1)
                Board.make_move(move, mark)
                return
            except (ValueError, IndexError):
                print("Coordinates should be from 1 to 3.")
                continue
            except exceptions.OccupiedCellException as e:
                print(e)
                continue


class AIPlayer:

    @staticmethod
    def random_move(mark: str):
        available_moves = Board.generate_moves()
        move = choice(available_moves)

        Board.make_move(move, mark)

    def easy_move(self, mark: str):
        """ Makes a random move """
        print("Making move level \"easy\"")
        self.random_move(mark)

    def medium_move(self, mark: str):
        """
        First checks for possible winning move, if there's
        no such move, checks if it can block the opponent's
        move, if no such move available again, makes a
        random move
        """
        print("Making move level \"medium\"")
        move = None
        opponent_mark = "O" if mark == "X" else "X"
        available_moves = Board.generate_moves()

        for test_move in available_moves:
            # checking for possible win
            Board.make_move(test_move, mark)
            if Board.check_game() == mark:
                move = (test_move[0], test_move[1])
                # if there's a winning move, stop searching
                break
            Board.unmake_move(test_move)

            # checking if it can block opponent's win
            Board.make_move(test_move, opponent_mark)
            if Board.check_game() == opponent_mark:
                move = (test_move[0], test_move[1])
            Board.unmake_move(test_move)

        if move is not None:
            Board.make_move(move, mark)
        else:
            self.random_move(mark)

    def minimax(self, alpha: int, beta: int, is_maximizing: bool, mark: str) -> int:
        """
        Applies minimax algorithm with alpha-beta pruning, no need
        depth since it's easy to reach the terminal state
        """
        score = Board.evaluate(mark)
        if score is not None:
            return score

        opponent_mark = "O" if mark == "X" else "X"
        available_moves = Board.generate_moves()
        if is_maximizing:
            value = -2
            for move in available_moves:
                Board.make_move(move, mark)
                value = max(value, self.minimax(alpha, beta, False, mark))
                Board.unmake_move(move)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = 2
            for move in available_moves:
                Board.make_move(move, opponent_mark)
                value = min(value, self.minimax(alpha, beta, True, mark))
                Board.unmake_move(move)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def hard_move(self, mark: str):
        print("Making move level \"hard\"")
        move = None
        best_eval = -2

        # generate all possible moves and calculate
        # their evaluation
        for temp_move in Board.generate_moves():
            Board.make_move(temp_move, mark)
            move_eval = self.minimax(-2, 2, False, mark)
            Board.unmake_move(temp_move)

            # finding the best evaluation
            if move_eval > best_eval:
                best_eval = move_eval
                move = (temp_move[0], temp_move[1])

        Board.make_move(move, mark)
