import random
import json


with open('words.json', 'r') as file:
    words =json.load(file)

# word = random.choice(words)

def play_game():
    hidden_word = random.choice(words)
    attempts = 6
    while attempts > 0:
        guess = str(input("Guess a word:"))
        if guess == hidden_word:
            print("That is the correct!!! CONGRATULATIONS!!!")
            break
        else:
            attempts -=1
            print(f"Wrong guess! you have {attempts} attempts left.")
            for i, j in zip(guess, hidden_word):
                if i in hidden_word and i == j:
                    print(f"{i} : 🍏")
                elif i in hidden_word and i != j:
                    print(f"{i} : 🍊")
                else:
                    print(f"{i} : ❌")
        if attempts == 0:
            print(f"GAME OVER!!! Correct word is {hidden_word}")

play_game()


# user_input = input("Spell A five letter word:")
# default_word = "apple"
# for i, j in zip(user_input, default_word):
#     if i == j:
#         print(f"{i} is correct")
#     else:
#         print(f"{i} is incorrect")


# def check_letter(letter, hidden_word, guessed_letters):
#     if letter in hidden_word:
#         guessed_letters.add(letter)
#         return True
#     else:
#         return False