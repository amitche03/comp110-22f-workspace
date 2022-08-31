"""One Shot Wordle"""

__author__ = "730562021"

user_word: str = input("What is your 6-letter guess?")
secret_word = "python"

while len(user_word) != len(secret_word):
    user_word = input("That was not 6 letters! Try again: ")

if user_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")



