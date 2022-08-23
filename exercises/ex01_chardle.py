"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730562021"

WORD: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
print("Searching for " + character + " in " + WORD )

if character in WORD:
    if character == WORD[0]:
        print( WORD[0] + " found at index 0")
    
    if character == WORD[1]:
        print(WORD[1] + " found at index 1")

    if character == WORD[2]:
        print(WORD[2] + " found at index 2")

    if character == WORD[3]:
        print(WORD[3] + " found at index 3")

    if character == WORD[4]:
        print(WORD[4] + " found at index 4")
else:
    print("No instances of " + character + " found in " + WORD)




