"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730562021"

WORD: str = input("Enter a 5-character word: ")
user_character: str = input("Enter a single character: ")
matching_characters: int = 0
print("Searching for " + user_character + " in " + WORD )

if user_character == WORD[0]:
        print( WORD[0] + " found at index 0")
        matching_characters += 1
    
if user_character == WORD[1]:
        print(WORD[1] + " found at index 1")
        matching_characters += 1

if user_character == WORD[2]:
        print(WORD[2] + " found at index 2")
        matching_characters += 1

if user_character == WORD[3]:
        print(WORD[3] + " found at index 3")
        matching_characters += 1

if user_character == WORD[4]:
        print(WORD[4] + " found at index 4")
        matching_characters += 1

if matching_characters == 0:
     print("No instances of " + user_character + " found in " + WORD)
else: 
    print(str(matching_characters) + " instances of " + user_character + " found in " + WORD)





