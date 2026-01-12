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
    while True:
        user_guess = input(f"Guess a number within the range {LOWEST_NUMBER} and {HIGHEST_NUMBER} inclusive or press 'q' to quit: ")
        result = validate_guess(user_guess, target)
        
        if result == 'q':
            return 'q'
        elif result is not None:
            return result

def validate_guess(user_guess, target, low=LOWEST_NUMBER, high=HIGHEST_NUMBER):
    if user_guess.lower() == 'q':
        return 'q'
    try:
        validated_guess = int(user_guess)
    except ValueError: 
        print("Invalid input.")
        return None
    if not low <= validated_guess <= high:
        print("Out of bounds.")
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
    
def reset_game(current_guesses):
    current_guesses = MAX_GUESSES
    return current_guesses


def play():
    target = pick_target_number()
    remaining_guesses = MAX_GUESSES

    while remaining_guesses > 0:
        guess = ask_for_guess(target)
        if guess == 'q':
            end_game_message()
            return
        if guess == target:
            end_game_message("Congratulations! You've guessed the correct number!")
            return
        remaining_guesses -= 1

    end_game_message("Out of guesses. Game over.")

if __name__ == "__main__":
    play()


