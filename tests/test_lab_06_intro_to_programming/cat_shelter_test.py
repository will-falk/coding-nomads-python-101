import lab_06_intro_to_programming.cat_shelter as cats

def test_pick_target_number():
    number = guess.pick_target_number()
    assert guess.LOWEST_NUMBER <= number <= guess.HIGHEST_NUMBER

def test_validate_guess():
    LOWEST_NUMBER = 0
    HIGHEST_NUMBER = 100
    TARGET = 50
    assert guess.validate_guess('q', TARGET) == 'q'
    assert guess.validate_guess('dog', TARGET) is None
    assert guess.validate_guess(TARGET -1, TARGET) == TARGET -1
    assert guess.validate_guess(TARGET +1, TARGET) == TARGET +1
    assert guess.validate_guess(LOWEST_NUMBER-1, TARGET) is None
    assert guess.validate_guess(HIGHEST_NUMBER+1, TARGET) is None
    assert guess.validate_guess(HIGHEST_NUMBER+1, TARGET) is None
