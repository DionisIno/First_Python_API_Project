from faker import Faker
import random
from data.data import *

faker_ru = Faker("ru_RU")
faker_en = Faker("En")
Faker.seed()

def get_person():
    yield Person(
        email=faker_ru.email(),
        user_name=faker_en.first_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        password=faker_en.password()
    )