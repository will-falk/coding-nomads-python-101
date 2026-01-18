from faker import Faker
from faker.providers import DynamicProvider

cuteness_provider = DynamicProvider(
     provider_name="cuteness",
     elements=["adorable", "endearing", "ugly to the point of cute", "a gorgeous feline"],
)

fake = Faker()
fake.add_provider(cuteness_provider)

def create_cat():
    name = fake.first_name().lower()
    color = fake.color_name().lower()
    age = fake.random_int(min=1, max=19)
    cuteness = fake.cuteness()
    
    cat = {
        "name": name,
        "color": color,
        "age": age,
        "cuteness": cuteness,
        "adopted": False
    }

    return cat

def create_shelter():
    pass

# generate some cats (use a random generator?)

# visit function...says what's available

# adopt function ... updates status as adopted

# drop off function ... receives a new cat

# assessment ... assigns characteristics - color, name, age, cuteness

#front desk ... greet, ask purpose...visit, adopt, drop off, exit
#effectively a router