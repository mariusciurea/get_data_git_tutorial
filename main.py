"""app main"""
from src.get_person_data import get_name_and_age

try:
    person = get_name_and_age(112)
    print(person)
except KeyError:
    print("Not a good user ID")


print("hello World!")
print("Marius added a new line")