## Hangman 💀
### How to Play
While in the `hyperskill-projects` directory, run the following commands to play the game:
```
cd hangman
```
```
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
Then, you will be asked to to choose a difficulty:
```
Enter difficulty (easy/medium/hard):
```
- `easy` difficulty chooses words from `easy_wordlist.txt` which contains 1400+ A1-A2 level words.
- `medium` difficulty chooses words from `medium_wordlist.txt` which contains 1300+ B1-B2 level words.
- `hard` difficulty chooses words from `hard_wordlist.txt` which contains 100+ C1+ level words.

After you choose the difficulty, you can start the game by making your first guess. Don't forget, you only have a total of 8 lives.

To see the results of the games you played so far, type `results` in the menu:
```
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > results
You won: 2 times.
You lost: 1 times.
```
If you're done playing, type `exit` to quit the game.
```
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > exit
```
