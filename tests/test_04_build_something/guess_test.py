import lab_04_build_something.guess as guess

def test_pick_target_number():
    number = guess.pick_target_number()
    assert guess.LOWEST_NUMBER <= number <= guess.HIGHEST_NUMBER

def test_validate_guess_valid():
    assert guess.validate_guess('50') == 50
    assert guess.validate_guess('dog') == None
    assert guess.validate_guess('0') == None
    assert guess.validate_guess('101') == None
    assert guess.validate_guess('q') == 'q'
    

