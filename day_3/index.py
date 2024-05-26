# data type

from colorama import init


age = 17
gpa = 2.8
name = "Shaikh"
is_active = True
has_banck_account = None
programming_knowlege = complex(5, 10)
hobbies = ["Dance", "Learning", "Javascript"]

print(type(age))  # initeger -> init
print(type(gpa))  # float
print(type(name))  # string -> str
print(type(hobbies))  # array -> list
print(type(is_active))  # boolean -> bool
print(type(has_banck_account))  # null -> NoneType
print(type(programming_knowlege))  # complex
convertedNumber = int("5")
print(convertedNumber + 5)  # convert string into number


# mutable -> also you can change -> list
# ummutable -> you can NOT change this bro -> tuple

# you can change list
# tupple NOT change
# dictionary

user_2 = {"name": "john", "age": 71}  # -> dict

print(user_2["name"])

# everything in python is object
