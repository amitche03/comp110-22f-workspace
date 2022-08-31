"""One Shot Wordle"""

__author__ = "730562021"


user_word: str = input("What is your 6-letter guess? ")
secret_word = "python"
i: int = 0
emoji_result = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(user_word) != len(secret_word):
    user_word = input("That was not 6 letters! Try again: ")


if user_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")


while i < len(secret_word): #Nested while loop
    if user_word[i] == secret_word[i]:
        emoji_result += GREEN_BOX
    else:
        chr_exists: bool = False
        alt_indices: int = 0
        while chr_exists is False and alt_indices < len(secret_word):
            if user_word[i] == secret_word[alt_indices]:  
                emoji_result += YELLOW_BOX
                chr_exists = True
            alt_indices = alt_indices + 1   
        if chr_exists is False:
            emoji_result += WHITE_BOX
    i = i + 1


print(emoji_result)



