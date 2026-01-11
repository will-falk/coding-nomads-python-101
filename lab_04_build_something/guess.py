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

def ask_for_guess():
    while True:
        user_guess = input(f"Guess a number within the range {LOWEST_NUMBER} and {HIGHEST_NUMBER} inclusive or press 'q' to quit: ")
        result = validate_guess(user_guess)
        
        if result == 'q':
            return 'q'
        elif result is not None:
            return result

def validate_guess(user_guess, low=LOWEST_NUMBER, high=HIGHEST_NUMBER):
    if user_guess.lower() == 'q':
        return 'q'
    try:
        validated_guess = int(user_guess)
    except ValueError: 
        print("Invalid input.")
        return None
    
    if not low <= validated_guess <= high:
        print("Out of bounds.")
    else:
        return validated_guess
    

def reset_game():
    #reset game variables to start a new game
    pass

def end_game():
    pass    

def play():
    ask_for_guess()
    #initialize
    #cycle through guesses
    #end or reset game
    #if quess is q, call end_game
    

if __name__ == "__main__":
    play()