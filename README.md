# JetBrains Academy Projects
Here you can find more information about each of my projects. 🚀
- NOTE: Some of them have slight alterations (mostly improvement) from what JetBrains Academy wanted.

Download and get access to the repository by running the following commands on your terminal:
```
git clone https://github.com/toprakware/jetbrains-projects.git
cd jetbrains-projects
```
- NOTE: If you don't have `git` installed, you can learn about how it's installed from [here.](https://github.com/git-guides/install-git)

# Projects

* ***[Hangman](https://github.com/toprakware/jetbrains-projects/edit/main/README.md#hangman-)***
* ***[Tic-Tac-Toe](https://github.com/toprakware/jetbrains-projects/edit/main/README.md#tic-tac-toe-with-ai-)***

## Hangman 💀
### How to Play
While in the `jetbrains-projects` directory, run the following commands to play the game:
```
cd hangman
python hangman.py
```
- NOTE: If `python` command could not be found even if you have Python installed, try using `python3` instead.


### About the Game
Well, you have probably played Hangman once in your life, so you should know the rules! Try to guess the chosen word before you run out of lives or you will be hanged. 🙂 

Once you run it, you can type `play` to start the game.
```
H A N G M A N

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > play
```
And then you will be asked to to choose a difficulty:
```
Enter difficulty (easy/medium/hard):
```
- `easy` difficulty chooses words from `easy_wordlist.txt` which contains 1400+ A1-A2 level words.
- `medium` difficulty chooses words from `medium_wordlist.txt` which contains 1300+ B1-B2 level words.
- `hard` difficulty chooses words from `hard_wordlist.txt` which contains 100+ C1+ level words.

When you choose the difficulty, you can start the game by making your first guess. Don't forget, you have a total of 8 lives.

To see the results of the games you played so far, type `results` in the menu:
```
H A N G M A N

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > results
```
```
You won: 2 times.
You lost: 1 times.
```
If you're done playing, type `exit` to quit the game.
```
H A N G M A N

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > exit
```


## Tic-Tac-Toe with AI ❌⭕❌
### How to Play
While in the `jetbrains-projects` directory, run the following command to play the game:
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
Enter the coordinates: > [row] [column]
```
- `easy` mode is the AI that generates random moves to play.
- `medium` mode is where we see some signs of intelligence. First, it checks that if it can make a winning move or not. If no such move is available, it then checks whether the opponent can win in their next move or not. If the opponent does, it blocks their winning move. If it can't do that either, it just makes a random move.
- `hard` mode is where the AI reaches superhuman level. Spoiler alert: it's impossible to win against, thanks to the [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm. I've also used [Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) and decreased the time it takes for the AI to make a move from ~1.3 seconds to ~0.09 seconds for the first move.

If you want to exit the game, simply type `exit`.
