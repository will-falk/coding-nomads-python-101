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
        "adoption status": False
    }

    return cat

def create_shelter(number_cats):
    shelter = []
    for x in range(number_cats):
        shelter.append(create_cat())
    return shelter

def print_cat(cat):
    blurb = f"Meet {cat['name']}!"
    for key in cat.keys():
        if not key == "name":
            blurb += f" Their {key} is {cat[key]}."
    print(blurb)

def visit(shelter):
    for cat in shelter:
        print_cat(cat)

def adopt(shelter, cat):
    shelter.remove(cat)
    return shelter

# drop off function ... receives a new cat

# assessment ... assigns characteristics - color, name, age, cuteness

#front desk ... 
# greet, ask purpose...visit, adopt, drop off, exit
#effectively a router