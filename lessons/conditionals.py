"""An example of conditional (if - else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: #Condition
    print("You guessed correctly!!! ") #Then Block
    print("Have a wonderful day!!! ")
else: # Else Block
    print("Sorry, you guessed incorrectly :(") #Then Block
    if guess > SECRET: #Condition
        print("You guessed too high! ") #Then Block
    else:
        print("You guessed too low! ") #Else Block

print("Game over. ")

