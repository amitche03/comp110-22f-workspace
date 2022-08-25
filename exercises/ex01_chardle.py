"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730562021"


user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()


user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Character must be a single character")
    exit()


matching_characters: int = 0
print("Searching for " + user_character + " in " + user_word)


if user_character == user_word[0]:
    print(user_word[0] + " found at index 0")
    matching_characters += 1
    

if user_character == user_word[1]:
    print(user_word[1] + " found at index 1")
    matching_characters += 1


if user_character == user_word[2]:
    print(user_word[2] + " found at index 2")
    matching_characters += 1


if user_character == user_word[3]:
    print(user_word[3] + " found at index 3")
    matching_characters += 1


if user_character == user_word[4]:
    print(user_word[4] + " found at index 4")
    matching_characters += 1


if matching_characters == 0:
    print("No instances of " + user_character + " found in " + user_word)
else:
    if matching_characters != 1:
        print(str(matching_characters) + " instances of " + user_character + " found in " + user_word)


if matching_characters == 1:
    print("1 instance of " + user_character + " found in " + user_word)