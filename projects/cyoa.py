"""Choose your own adventure."""

__author__ = "730562021"

from random import randint
points: int 
player: str 
HORSE_EMOJI: str = "\U0001F434"
DOG_EMOJI: str = "\U0001F436"
MONKEY_EMOJI: str = "\U0001F435"
horse: list[int] = [80, 60, 80, 80]
dog: list[int] = [80, 90, 60, 60]
monkey: list[int] = [60, 70, 40, 70]
chosen_animal : str = ""

def main() -> None:
    """Entrypoint of game."""
    global points
    points = 0
    greet()
    first_choice: str = input(f"{player} you like to continue? ")
    if first_choice == "yes":
        animals()
        points += gameplay(chosen_animal)
        first_choice = input(f"{player} you like to continue? \n Enter 'yes' or 'no' ")
    if first_choice == "no": 
        print(f"{player} thank you for playing. You have accumulated {points} adventure points. ")
    print(f"Here are your horse's final statistics.\n Health, Affection, Hunger, Speed. \n {horse} ")

# A line about animals final stats. 


def greet() -> None:
    """Greeting to user."""
    global player 
    global points
    player = input("Hello! What is your name? ")
    print(f"Hello, {player} welcome to the zoo! \n In this game you will choose an animal to nurture. \n Based off of its given stats, your animal requires various forms of care. \n Your decisions directly affects its health. ")
    print(f"Even more importantly, your decisions will affect your points. \n Currently, you have {points} adventure points. ")


def animals() -> None:
    """Allows the user to choose its animal. """
    global points
    global chosen_animal
    """Displays the stats of different animals and lets the user choose the animal they want. """
    print("Each animal has different stats. Listed as follows: Health, Affection, Hunger, and Speed. ")
    print("Each animals stats will change based on your actions in the game.")
    print("In this game you can choose to have a Horse, Dog, or Monkey. ")
    print("Horse", HORSE_EMOJI, "\n Health: 80 \n Affection: 60 \n Hunger: 80 \n Speed: 80")
    print("Dog", DOG_EMOJI, "\n Health: 80 \n Affection: 90 \n Hunger: 60 \n Speed: 60")
    print("Monkey", MONKEY_EMOJI, "\n Health: 60 \n Affection: 70 \n Hunger: 40 \n Speed: 70")
    chosen_animal = input(f"{player} what animal will you choose? Press 1 for Horse, 2 for Dog, and 3 for Monkey. ")
    while (chosen_animal != "1") and (chosen_animal != "2") and (chosen_animal != "3"):
        print("Sorry that was not a valid input. ")
        chosen_animal = input(f"{player} what animal will you choose? Enter 1 for Horse, 2 for Dog, and 3 for Monkey. ")
    points += 5


def gameplay(animal: str) -> int: #Procedure
    """Allows the user to make choices on how to care for its animal. """
    global horse
    global dog
    global monkey
    SAD_EMOJI: str = "\U00002639"
    choices_points: int = 0
    user_animal: str = ""
    turns: int = 0
    if animal == "1":
        user_animal = "Horse"
    elif animal == "2":
        user_animal = "Dog"
    else:
        user_animal = "Monkey"
    print(f"In this portion of the game, you will choose how to take care of your {user_animal}.")
    print(f"The choices you make affect your {user_animal}'s statistics and overall game points.")
    print("Respond to each promopt with either 'y' or 'n' ")
    print("Let's Begin.")
    
    
    while turns <= 2: 
        if user_animal == "Horse":
            horse_choice_one: str = ""
            horse_choice_one = input("Would you like to take you horse on a run? ")
            if horse_choice_one == "y":
                print(f"{player}'s horse really appreciated its run. ")
                random_speed_increase: int = randint(0,20)
                horse[3] += random_speed_increase
                horse[1] += 5
                print(f"Your horse's speed has increased by {random_speed_increase} points! ")
                print("Your horse's affection has increased by 5 points.")
                print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse}")
                choices_points += 10
                print(f"You gained 10 adventure points. ")
            else:
                print("Your horse will remember that. ")
                horse[0] -= 5
                horse[1] -= 10
                choices_points -= 5
                print(f"{player}, your horse's health has decreased by 5 points. ")
                print(f"{player}, your horse's affection has decreased by 10 points. ")
                print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse} ")
                print("You lost 5 adventure points. ")
            turns += 1
            horse_choice_two: str = ""
            horse_choice_two = input("Would you like to feed your horse a carrot? ")
            if horse_choice_two == "y":
                print(f"{player}'s horse loved its snack! ")
                random_hunger_decrease: int = randint(0, 10)
                horse[2] -= random_hunger_decrease
                horse[1] += 10 
                print(f"Your horse's hunger has decreased by {random_hunger_decrease} points! ")
                print("Your horse's affection has increased by 10 points.")
                print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse}")
                choices_points += 10
                print(f"You gained 10 adventure points. ")
            else: 
                print("Don't let your horse go hungry! ")
                horse[2] += 5
                horse[1] -= 10
                horse[0] -= 5
                choices_points -= 10
                print(f"{player}, your horse's health has decreased by 5 points. ")
                print(f"{player}, your horse's affection has decreased by 10 points. ")
                print(f"{player}, your horse's health has decreased by 5 points. ")
                print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse} ")
                print("You lost 10 adventure points. ")
            turns += 1


        if user_animal == "Dog":
            dog_choice_one: str = ""
            dog_choice_one = input("Would you like to take your dog on a walk? ")
            if dog_choice_one == "y":
                print(f"{player}'s dog really appreciated its walk. ")
                random_affection_increase: int = randint(0,20)
                dog[1] += random_affection_increase
                dog[2] += 5
                print(f"Your dog's affection has increased by {random_affection_increase} points! ")
                print("Your dog's hunger has increased by 5 points.")
                print(f"Here are your dogs new statistics.\n Health, Affection, Hunger, Speed. \n {dog}")
                choices_points += 10
                print(f"You gained 10 adventure points. ")
            else: 
                print("But your dog is such a good boy.", SAD_EMOJI)
                dog[1] -= 5
                dog[0] -= 10
                choices_points -= 5 
                print(f"{player}, your dog's affection has decreased by 5 points. ")
                print(f"{player}, your dog's health has decreased by 10 points. ")
                print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog} ")
                print("You lost 5 adventure points. ")
            turns += 1
            dog_choice_two: str = input("Would you like to give your dog a treat? ")
            if dog_choice_one == "y":
                print(f"{player}'s dog is so happy!")
                dog[1] += 10
                dog[2] -= 5
                choices_points += 10
                print(f"Your dog's affection has increased by 10 points! ")
                print("Your dog's hunger has decreased by 5 points.")
                print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog}")
                print(f"You gained 10 adventure points. ")
            else: 
                print("All dogs deserve treats.", SAD_EMOJI)
                dog[1] -= 5
                dog[0] -= 10
                choices_points -= 5 
                print(f"{player}, your dog's affection has decreased by 5 points. ")
                print(f"{player}, your dog's health has decreased by 10 points. ")
                print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog} ")
                print("You lost 5 adventure points.")
            turns += 1


        if user_animal =="Monkey":
            monkey_choice_one: str = ""
            monkey_choice_one = input("Would you like to feed your monkey? ")
            if monkey_choice_one == "y":
                print(f"{player}'s monkey is satisfied. ")
                random_hunger_decrease: int = randint(0,20)
                monkey[2] -= random_hunger_decrease
                monkey[0] += 10
                print(f"Your monkey's hunger has decreased by {random_hunger_decrease} points! ")
                print("Your monkey's health has increased by 10 points.")
                print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey}")
                choices_points += 15
                print("You gained 15 adventure points. ")
            else:
                print("Your monkey is going to be hungry. ")
                monkey[0] -= 5
                monkey[1] -= 10
                choices_points -= 5
                print(f"{player}, your monkey's health has decreased by 5 points. ")
                print(f"{player}, your monkey's affection has decreased by 10 points. ")
                print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey} ")
                print("You lost 5 adventure points. ")
            turns += 1
            monkey_choice_two: str = ""
            monkey_choice_two = input("Would you like to play with your monkey? ")
            if monkey_choice_two == "y":
                print(f"{player}'s monkey loves attention. ")
                monkey[1] += 20
                print(f"Your monkeys's affection has increased by 20 points! ")
                print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey}")
                choices_points += 10
                print(f"You gained 10 adventure points. ")
            else: 
                print("Your monkey is lonely.", SAD_EMOJI)
                monkey[1] -= 10
                horse[0] -= 5
                choices_points -= 10
                print(f"{player}your monkey's health has decreased by 5 points. ")
                print(f"{player}, your monkey's affection has decreased by 10 points. ")
                print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey} ")
                print("You lost 10 adventure points. ")
            turns += 1
        turns += 1


            #What to print if points are greater than 0 or leess than 0 
    if choices_points < 0:
        print(f"Overall, you have now {choices_points} adventure points. ")
    else:
        print(f"Overall, you now have gained {choices_points} adventure points. ")
    return choices_points

if __name__ == "__main__":
    main()