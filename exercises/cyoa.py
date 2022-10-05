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
user_animal_list: list[int] = []
chosen_animal: int = 0
user_animal: str = ""
do_you_want_to_play_again: str = ""


def greet() -> None:
    """Greeting to user."""
    print("Hello, welcome to this game. ")
    global player 
    player = input("What is your name? ")


def main() -> None:
    """Entrypoint of game."""
    global points
    global chosen_animal
    global do_you_want_to_play_again
    points = 0
    greet()
    animals()
    points += gameplay(chosen_animal)
    if points > 0 and do_you_want_to_play_again == "":
        print(f"{player} thank you for playing. You have earned {points} adventure points. ")
        print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
    elif points == 0 and do_you_want_to_play_again == "":
        print(f"{player}, you have gained no points. ")
        print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
    elif points < 0 and do_you_want_to_play_again == "": 
        print(f"{player} thank you for playing. You have {points} adventure points. ")
        print(f"Here are your {user_animal}'s final statistics.\n Health, Affection, Hunger, Speed. \n {user_animal_list} ")   
    if do_you_want_to_play_again == "n": 
        if points > 0:
            print(f"{player} thank you for playing. You have earned {points} adventure points. ")
            print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
        elif points == 0:
            print(f"{player}, you have gained no points. ")
            print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
        else: 
            print(f"{player} thank you for playing. You have {points} adventure points. ")
            print(f"Here are your {user_animal}'s final statistics.\n Health, Affection, Hunger, Speed. \n {user_animal_list} ") 
        exit()
    while do_you_want_to_play_again == "y":
        points = 0
        greet()
        animals()
        points += gameplay(chosen_animal)
        if points > 0:
            print(f"{player} thank you for playing. You have earned {points} adventure points. ")
            print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
        elif points == 0:
            print(f"{player}, you have gained no points. ")
            print(f"Here are your {user_animal}'s final statistics. \n Health, Affection, Hunger, Speed. \n {user_animal_list} ")
        else: 
            print(f"{player} thank you for playing. You have lost {points} adventure points. ")
            print(f"Here are your {user_animal}'s final statistics.\n Health, Affection, Hunger, Speed. \n {user_animal_list} ")   


def animals() -> None:
    """Allows the user to choose its animal."""
    global points
    global chosen_animal
    global player
    print(f"Hello, {player} welcome to the zoo! \n In this game you will choose an animal to nurture. \n Based off of its given stats, your animal requires various forms of care. ")
    print(f"Even more importantly, your decisions will affect your points. \n Currently, you have {points} adventure points. ")
    """Displays the stats of different animals and lets the user choose the animal they want. """
    print("Each animal has different stats. Listed as follows: Health, Affection, Hunger, and Speed. ")
    print("Each animals stats will change based on your actions in the game.")
    print("In this game you can choose to have a Horse, Dog, or Monkey. ")
    print("Horse", HORSE_EMOJI, "\n Health: 80 \n Affection: 60 \n Hunger: 80 \n Speed: 80")
    print("Dog", DOG_EMOJI, "\n Health: 80 \n Affection: 90 \n Hunger: 60 \n Speed: 60")
    print("Monkey", MONKEY_EMOJI, "\n Health: 60 \n Affection: 70 \n Hunger: 40 \n Speed: 70")
    chosen_animal = int(input(f"{player} what animal will you choose? Press 1 for Horse, 2 for Dog, and 3 for Monkey. "))
    while (chosen_animal != 1) and (chosen_animal != 2) and (chosen_animal != 3):
        print("Sorry that was not a valid input. ")
        chosen_animal = int(input(f"{player} what animal will you choose? Enter 1 for Horse, 2 for Dog, and 3 for Monkey. "))
    points += 5
    print("You gained 5 adventure points. ")


def gameplay(animal: int) -> int: 
    """Allows the user to make choices on how to care for its animal."""
    global player
    global horse
    global dog
    global monkey
    global user_animal
    global user_animal_list
    global do_you_want_to_play_again
    SAD_EMOJI: str = "\U00002639"
    choices_points: int = 0
    first_choice: str = ""
    if animal == 1:
        user_animal = "Horse"
    elif animal == 2:
        user_animal = "Dog"
    else:
        user_animal = "Monkey"
    print(f"In this portion of the game, you will choose how to take care of your {user_animal}.")
    print(f"The choices you make affect your {user_animal}'s statistics and overall game points.")
    print("Respond to each promopt with either 'y' or 'n' ")
    print("Let's Begin.")
    if user_animal == "Horse":
        user_animal_list = horse
        horse_choice_one: str = ""
        horse_choice_one = input("Would you like to take you horse on a run? ")
        if horse_choice_one == "y":
            print(f"{player}'s horse really appreciated its run. ")
            random_speed_increase: int = randint(0, 20)
            horse[3] += random_speed_increase
            horse[1] += 5
            print(f"Your horse's speed has increased by {random_speed_increase} points! ")
            print("Your horse's affection has increased by 5 points.")
            print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse}")
            choices_points += 10
            print("You gained 10 adventure points. ")
        else:
            print("Your horse will remember that. ")
            horse[0] -= 5
            horse[1] -= 10
            choices_points -= 5
            print(f"{player}, your horse's health has decreased by 5 points. ")
            print(f"{player}, your horse's affection has decreased by 10 points. ")
            print(f"Here are your horse's new statistics.\n Health, Affection, Hunger, Speed. \n {horse} ")
            print("You lost 5 adventure points. ")
        first_choice = input(f"{player} would you like to continue? \n Enter 'y' or 'n' ")
        if first_choice == "n":
            do_you_want_to_play_again = ""
            return choices_points
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
            print("You gained 10 adventure points. ")
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
        do_you_want_to_play_again = input("Do you want to play again? \n Enter 'y' or 'n' ")
    if user_animal == "Dog":
        user_animal_list = dog
        dog_choice_one: str = ""
        dog_choice_one = input("Would you like to take your dog on a walk? ")
        if dog_choice_one == "y":
            print(f"{player}'s dog really appreciated its walk. ")
            random_affection_increase: int = randint(0, 20)
            dog[1] += random_affection_increase
            dog[2] += 5
            print(f"Your dog's affection has increased by {random_affection_increase} points! ")
            print("Your dog's hunger has increased by 5 points.")
            print(f"Here are your dogs new statistics.\n Health, Affection, Hunger, Speed. \n {dog}")
            choices_points += 10
            print("You gained 10 adventure points. ")
        else: 
            print("But your dog is such a good boy.", SAD_EMOJI)
            dog[1] -= 5
            dog[0] -= 10
            choices_points -= 5 
            print(f"{player}, your dog's affection has decreased by 5 points. ")
            print(f"{player}, your dog's health has decreased by 10 points. ")
            print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog} ")
            print("You lost 5 adventure points. ")
        first_choice = input(f"{player} would you like to continue? \n Enter 'y' or 'n' ")
        if first_choice == "n": 
            do_you_want_to_play_again = ""
            return choices_points
        dog_choice_two: str = input("Would you like to give your dog a treat? ")
        if dog_choice_two == "y":
            print(f"{player}'s dog is so happy!")
            dog[1] += 10
            dog[2] -= 5
            choices_points += 10
            print("Your dog's affection has increased by 10 points! ")
            print("Your dog's hunger has decreased by 5 points.")
            print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog}")
            print("You gained 10 adventure points. ")
        else: 
            print("All dogs deserve treats.", SAD_EMOJI)
            dog[1] -= 5
            dog[0] -= 10
            choices_points -= 5 
            print(f"{player}, your dog's affection has decreased by 5 points. ")
            print(f"{player}, your dog's health has decreased by 10 points. ")
            print(f"Here are your dog's new statistics.\n Health, Affection, Hunger, Speed. \n {dog} ")
            print("You lost 5 adventure points.")
        do_you_want_to_play_again = input("Do you want to play again? \n Enter 'y' or 'n' ")
    if user_animal == "Monkey":
        user_animal_list = monkey
        monkey_choice_one: str = ""
        monkey_choice_one = input("Would you like to feed your monkey? ")
        if monkey_choice_one == "y":
            print(f"{player}'s monkey is satisfied. ")
            random_hunger_decrease = randint(0, 20)
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
        first_choice = input(f"{player} would you like to continue? \n Enter 'y' or 'n' ")
        if first_choice == "n": 
            do_you_want_to_play_again = ""
            return choices_points
        monkey_choice_two: str = ""
        monkey_choice_two = input("Would you like to play with your monkey? ")
        if monkey_choice_two == "y":
            print(f"{player}'s monkey loves attention. ")
            monkey[1] += 20
            print("Your monkeys's affection has increased by 20 points! ")
            print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey}")
            choices_points += 10
            print("You gained 10 adventure points. ")
        else: 
            print("Your monkey is lonely.", SAD_EMOJI)
            monkey[1] -= 10
            horse[0] -= 5
            choices_points -= 10
            print(f"{player} your monkey's health has decreased by 5 points. ")
            print(f"{player}, your monkey's affection has decreased by 10 points. ")
            print(f"Here are your monkey's new statistics.\n Health, Affection, Hunger, Speed. \n {monkey} ")
            print("You lost 10 adventure points. ")
        do_you_want_to_play_again = input("Do you want to play again? \n Enter 'y' or 'n' ") 
    return choices_points


if __name__ == "__main__":
    main()