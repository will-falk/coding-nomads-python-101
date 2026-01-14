import random

#just going to roll my own guessing game
#user has 5 tries to guess a number between 1 and 100
#game gives feedback of whether each guess is above or below the number
#after 5th fail, number is revealed
#user can continue to press end to stop playing

LOWEST_NUMBER = (1)
HIGHEST_NUMBER = (100)
MAX_GUESSES = (5)

def pick_target_number(low=LOWEST_NUMBER, high=HIGHEST_NUMBER):
    return random.randint(low, high)

def ask_for_guess(target):
        user_guess = input(f"Guess a number within the range {LOWEST_NUMBER} and {HIGHEST_NUMBER} inclusive or press 'q' to quit: ")
        return validate_guess(user_guess, target)

def validate_guess(user_guess, target, low=LOWEST_NUMBER, high=HIGHEST_NUMBER):
    if isinstance(user_guess, str) and user_guess.lower() == 'q':
            return 'q'

    try:
        validated_guess = int(user_guess)
    except (ValueError, TypeError):
        print("Invalid input. Integers only.")
        return None

    if not low <= validated_guess <= high:
        print("Out of bounds.")
        return None
    if validated_guess < target:
        print("Higher.")
        return validated_guess
    if validated_guess > target:
        print("Lower.")
        return validated_guess
    if validated_guess == target:
        print("Correct!")
        return validated_guess

def end_game_message(message="Thanks for playing! Goodbye."):
    print(message)

def play():
    target = pick_target_number()
    remaining_guesses = MAX_GUESSES

    while remaining_guesses >= 1:
        remaining_guesses -= 1
        guess = ask_for_guess(target)
        
        if guess == 'q':
            end_game_message()
            return

        if guess == target:
            end_game_message("Congratulations! You've guessed the correct number!")
            return

    end_game_message("Out of guesses. Game over. The number was {TARGET}.")

if __name__ == "__main__":
    play()


