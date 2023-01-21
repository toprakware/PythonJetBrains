import random
import string

print("H A N G M A N")

word_list = ["python", "java", "swift", "javascript"]
win_count, lose_count = 0, 0

while True:

    player_input = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")

    if player_input.lower() == "play":
        attempts = 8
        secret_word = random.choice(word_list)
        guess_string = ""

        while True:
            print()

            for char in secret_word:
                if char in guess_string:
                    print(char, end="")
                else:               
                    print("-", end="")

            guess = input("\nInput a letter: ")

            try:
                int(guess)
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            except ValueError:
                pass

            if len(guess) != 1:
                print("Please, input a single letter.\n")
                continue
            elif guess.isupper() or guess not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if guess in guess_string:
                print("You've already guessed this letter.")
                continue

            elif guess not in secret_word:
                print("That letter doesn't appear in the word.")
                attempts -= 1

            if attempts == 0:
                print("\nYou lost!")
                lose_count += 1
                break

            guess_string += guess

            if all([letter in guess_string for letter in secret_word]):
                print(f"\nYou guessed the word {secret_word}!\nYou survived!")
                win_count += 1
                break

    elif player_input.lower() == "results":
        print(f"You won: {win_count} times.\nYou lost: {lose_count} times.")
    
    elif player_input.lower() == "exit":
        break
    else:
        continue
