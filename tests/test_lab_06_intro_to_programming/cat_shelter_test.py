import lab_06_intro_to_programming.cat_shelter as cats

def test_create_cat():
    cat = cats.create_cat()
    
    assert set(cat.keys()) == {"name", "color", "age", "cuteness", "adoption status"}
    assert isinstance(cat["name"], str)
    assert cat["name"] == cat["name"].lower()
    
    assert isinstance(cat["color"], str)
    assert cat["color"] == cat["color"].lower()
    
    assert isinstance(cat["age"], int)
    assert 1 <= cat["age"] <= 19
    
    assert cat["adoption status"] == False

def test_create_shelter():
    shelter_size = 5
    assert len(cats.create_shelter(shelter_size)) == shelter_size

def test_print_cat(capsys):
    cat = cats.create_cat()
    cats.print_cat(cat)
    captured = capsys.readouterr()
    assert captured.out.startswith("Meet")
