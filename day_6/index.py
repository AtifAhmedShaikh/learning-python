from email.policy import default
import time


user_time = None


hours = time.strftime("%H")  # hours
minutes = time.strftime("%M")
second = time.strftime("%S")


user_time = int(input("Enter "))

number = 10

match number:
    case 10:
        print("5 Number")
    case 8:
        print("8 Number")
    case _: # default case
        print("I don't know Number")
