from random import choice
from string import ascii_lowercase

win_count, lose_count = 0, 0
print("H A N G M A N")


def game():
    global lose_count, win_count

    difficulty = input("Enter difficulty (easy/medium/hard): ")
    while difficulty.lower() not in ("easy", "medium", "hard"):
        difficulty = input("Difficulty must be easy, medium or hard: ")

    with open("{}_wordlist.txt".format(difficulty), "r") as wordlist:
        secret_word = choice(wordlist.readlines()).replace("\n", "")

    board = list(len(secret_word) * "_")
    attempts = 8
    guessed = []

    while True:

        print("\n" + "".join(board))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("Please, input a single letter.\n")
            continue
        if guess.isupper() or guess not in ascii_lowercase or type(guess) is int:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in guessed:
            print("You've already guessed this letter.")
            continue

        for index, value in enumerate(secret_word):
            if guess == value:
                board[index] = guess

            guessed.append(guess)

        if all([letter in guessed for letter in secret_word]):
            print("\nYou guessed the word {}!\nYou survived!".format(secret_word))
            win_count += 1
            return
        if guess not in secret_word:
            attempts -= 1
            if attempts == 0:
                print("\nYou have no attempts left. You lost! The secret word was {}".format(secret_word))
                lose_count += 1
                return
            else:
                print("That letter doesn't appear in the word. You have {} attempts left.".format(attempts))


while True:

    player_input = input("\nType \"play\" to play the game, " +
                         "\"results\" to show the scoreboard, and \"exit\" to quit: ").lower()

    if player_input == "play":
        game()
    elif player_input == "results":
        print("You won: {} times.\nYou lost: {} times.".format(win_count, lose_count))
    elif player_input == "exit":
        quit()
    else:
        continue
