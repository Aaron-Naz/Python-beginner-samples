# Booleans

# print(True)
# print("True")

# print(type(True))  # This type is a bool
# print(type("True"))  # This type is a string

# Testing whether statements are correct
# print(5 == 5)
# print(6 == 5)

# Incorporating the if statement with a bool
# x = 11
# y = 5
# if x % y == 0:
#     print(True)
# else:
#     print(False)

# While loop
# number = 1
# while number < 4:
#     print(number)
#     if number == 4:
#         break
#     number = number + 1

# Incorporating the else statement within the while loop
# number = 2
# while number < 4:
#     print(number)
#     number = number + 1
# else:
#     print("number is no longer less than 4")


# If statement
number = int(input("Type in an integer: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
