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
    #prompt user for guess input
    pass

def evaluate_guess(guess, target):
    #evaluate_guess checks if guess is correct, too high, or too low
    pass

def reset_game():
    #reset game variables to start a new game
    pass

def end_game():
    pass

def play():
    #initialize
    #cycle through guesses
    #end or reset game
    pass

if __name__ == "__main__":
    # ...call play
    play()