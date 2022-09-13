"""A final attempt at wordle."""

__author__ = "730562021"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(analyzed_string: str, looking_for_character: str) -> bool:
    """Looks through argument 1 to see if argument 2 is present."""
    assert len(looking_for_character) == 1
    i: int = 0
    while i < len(analyzed_string):
        if analyzed_string[i] == looking_for_character:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char to analyze string for matching characters from guessed word. If the guessed word has characaters do not that match those of the secret word, this function concatenates white and yellow boxes."""
    assert len(guess) == len(secret)
    i: int = 0 
    emoji_result: str = ""
    
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        i += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """Given an integer of a certain value, prompt the user for a guess until they provide a guess of expected length."""
    user_word: str = input(f"Enter a {expected_length} character word: ")
    
    while expected_length != len(user_word):
        user_word = input(f"That wasn't {expected_length} chars! Try again: ")
    else:
        return user_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    won: bool = False
    
    while turn <= 6 and won is not True:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            won = True
            print(f"You won in {turn}/6 turns! ")
        turn += 1 
    if turn > 6 and won is False:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()