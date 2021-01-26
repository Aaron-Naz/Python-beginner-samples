# Strings

# We have already covered strings, integers, floats, booleans and lists

# Integers, floats and booleans are all considered to be simple data types
# They cannot be broken down!

# Lists and strings are different! They are made up of smaller pieces which CAN be broken down.

# We already know what strings are
# print("Hello, world!")
# print(type("Hello, world!"))

# Operations on strings
# Addition sign concatenation
# Greeting = "Hello"
# Name = "Aaron"
# print(Greeting + Name)

# * operator
# print(Name*3)
# print((Greeting + Name)*3)

# Index operator
# Name = "Aaron"
# print(Name[2])  # Prints 2nd element

# Slicing strings
# print(Name[0:5])  # Prints from 0th element until (but not including) 5th element
# print(Name[:2])  # Prints up to (but not including) 2nd element
# print(Name[2:])  # Prints from 2nd element onwards

# Lowercase and uppercase
# Name = "Aaron"
# print(Name.lower())
# print(Name.upper())
#
# # Count how many times a character appears in a string
# print(Name.count("n"))
#
# # Replace specific characters with other characters
# print(Name.replace("a", "p"))
# New_Name = Name.replace("a", "p")
# print(New_Name)
#
# # Finding the length of a string
# print(len(Name))

# Format strings
# your_name = input("Your name is: ")
# greeting = "Hello {}".format(your_name)
# print(greeting)

# Each letter in Python is assigned to a specific number!
# print("orange" < "strawberry")
# print(ord("o"))  # Find out what number is assigned to the letter "o"
# print(chr(78))  # Find out what character is assigned to the number "78"

# in and not operators
# fruit = "banana"
# print("a" in fruit)
# print("s" not in fruit)
# print("j" in fruit)

# Incorporate a few things we've learnt so far
x = "Hello"
y = ""

for character in x:
    y = y + character.upper()
print(y)
