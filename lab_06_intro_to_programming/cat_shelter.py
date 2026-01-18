from faker import Faker
from faker.providers import DynamicProvider

cuteness_provider = DynamicProvider(
     provider_name="cuteness",
     elements=["adorable", "endearing", "ugly to the point of cute", "a gorgeous feline"],
)

fake = Faker()
fake.add_provider(cuteness_provider)


#initiate array of dictionaries

# generate some cats (use a random generator?)

# visit function...says what's available

# adopt function ... updates status as adopted

# drop off function ... receives a new cat

# assessment ... assigns characteristics - color, name, age, cuteness

#front desk ... greet, ask purpose...visit, adopt, drop off, exit
#effectively a router


