from board import Board
from players import AIPlayer, HumanPlayer


ai = AIPlayer()
human = HumanPlayer()


def match_player(player: str, mark: str):
    match player:
        case "user":
            human.user_move(mark)
        case "easy":
            ai.easy_move(mark)
        case "medium":
            ai.medium_move(mark)
        case "hard":
            ai.hard_move(mark)


def main():
    while True:
        player1, player2 = Board.get_commands()
        Board.game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        Board.print_board()

        while True:
            match_player(player1, "X")
            Board.print_board()
            winner = Board.check_game()
            if winner is not None:
                print("X wins" if winner != "Draw" else "Draw")
                break

            match_player(player2, "O")
            Board.print_board()
            winner = Board.check_game()
            if winner is not None:
                print("O wins" if winner != "Draw" else "Draw")
                break


if __name__ == "__main__":
    main()
