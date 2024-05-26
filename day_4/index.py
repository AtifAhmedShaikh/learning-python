from msilib import PID_TITLE


user_name = None
user_age = None

print(2 + 5)
print(2 - 5)
print(5 * 5)
print(10 / 5)
print(15 // 6)
print(2 % 5)
print(5**3)  # 5*5*5


def calculateNumber(number_1: int, number_2: int):
    result = int(number_1) + int(number_2)
    print(result)
    return result


calculateNumber(3, 5)

user_name = input("Enter you name \n")
user_age = input("Enter you age \n")  # input always return value in string

print(user_name[0], user_age)

# print all charaters one by one
for c in user_name:
    if c != " ":  # without spaces
        print(c)


# string slice

name_3 = "hey22 bro how are you"
name_3[0:3]  # return first index to third -> hey2
name_3.capitalize()  # capitalize first letter
len(name_3)  # length of string
print(name_3[0:4])
