# 1. Assigning variables and performing calculations with them

# x = 8
# y = 4
#
# print(x + y)  # Addition
#
# print(x / y)  # Division
#
# print(x - y)  # Subtraction
#
# print(x * y)  # Multiplication


# 2. Lists
# even_numbers = list(range(0, 101, 2))  # Creates list of even numbers
# print(even_numbers[:10])  # Prints first 10 elements
# print(len(even_numbers))  # Prints length of list
# even_numbers.append(102)  # Adds 102 to the end of the list


# 3. If statement
# x = 25
# if x % 5 == 0:  # Checks if x is divisible by 5
#     print("This number is divisible by 5")
# else:
#     print("This number is not divisible by 5")


# 4. For loop
# for numbers in range(0, 6):  # Sets range with limit of 6 so that 0-5 is included
#     print(numbers)


# 5. Draw a pentagon in turtle
# import turtle  # Import turtle
#
# turtle.bgcolor("black")  # turtle set-up
# turtle.pensize(2)
# turtle.color("red")
# turtle.speed(0)
#
# for i in range(5):  # pentagon has 5 sides so iterate 5 times
#     turtle.forward(100)  # length chosen for sides of pentagon
#     turtle.left(72)  # exterior angle of a pentagon
# turtle.done()


# 6. Create a function that tests whether three numbers are a Pythagorean triple

# def pythagorean_triple(a, b, c):
#     if ((a**2) + (b**2)) == (c**2):
#         return "These numbers are considered Pythagorean triples!"
#     else:
#         return "These numbers are not considered Pythagorean triples!"
#
#
# print(pythagorean_triple(3, 4, 5))
# print(pythagorean_triple(1, 2, 3))


# 7. Spot the error

# Sample code with error in it
# n = 5
# while n > 0
# n = n + 1
#     print(n)

# Corrected code
# n = 5
# while n > 0:
#     n = n + 1
#     print(n)  # This code is now corrected in syntax, however it'll run forever so don't run it!


# 8. Create 2 lists of 5 variables and plot them against each other

import matplotlib.pyplot as plt

list1 = [1, 2, 3, 4, 5]
list2 = [5, 10, 15, 20, 25]

plt.plot(list1, list2, c="red", linewidth=1, label="One line", linestyle="dashed",
         marker="o", markerfacecolor="black", markersize=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Quiz question 8")
plt.legend()
plt.show()
