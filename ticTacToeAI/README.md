## Tic-Tac-Toe with AI ❌⭕❌
### How to Play
While in the `hyperskill-projects` directory, run the following command to play the game:
```
python ticTacToeAI.py
```
- NOTE: If `python` command could not be found even if you have Python installed, try using `python3` instead.

### About the Game
This is a classic Tic-Tac-Toe game in which you can play against a friend or an AI.

Once you run it, you will be asked to enter a command. Here's the structure: 
```
Input command: > start [player1] [player2]
```
`player1` will always be X while `player2` will always be O. Here are all the available player modes:
- `user` mode is basically the human player who will be asked to enter coordinates to make their moves. You can think the game board as a 3x3 matrix:
```
---------
|       |
|       |
|       |
---------
Enter the row: > [row]
Enter the column: > [column]
```
- `easy` mode is the AI that generates random moves to play.
- `medium` mode is where we see some signs of intelligence. First, it checks that if it can make a winning move or not. If no such move is available, it then checks whether the opponent can win in their next move or not. If the opponent does, it blocks their winning move. If it can't do that either, it just makes a random move.
- `hard` mode is where the AI reaches superhuman level. Spoiler alert: it's impossible to win against, thanks to the [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm. I've also used [Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) and decreased the time it takes for the AI to make the first move from ~1.3 seconds to ~0.09 seconds.

If you want to exit the game, simply type `exit`.

Thanks to Sebastian Lague ([@SebLague](https://github.com/SebLague)) for his incredible [video](https://www.youtube.com/watch?v=l-hh51ncgDI) that helped me a lot on making sense of the Minimax algorithm and Alpha-beta pruning.
