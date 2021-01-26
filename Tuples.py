# Tuples in Python

# Conventionally, tuples look like this:
# fruit = ("apples", 4, "bananas", 5, "oranges", 6)
# print(type(fruit))


# list_of_fruit = ["apples", 4, "bananas", 5, "oranges", 6]
# print(type(list_of_fruit))

# We can modify elements in a list
# list_of_fruit[0] = "strawberries"
# print(list_of_fruit)

# We can't modify elements in a tuple
# fruit[0] = "strawberries"
# print(fruit)  # This doesn't run since tuple elements can be modified

# We can perform similar operations on tuples like we do with lists

# Slicing tuples
# print(fruit[0:3])

# Recalling elements within a tuple
# print(fruit[0])

# Concatenation of tuples
# fruit = fruit[:4] + ("cherries", 10)
# print(fruit)

# Tuples with one element
# x = (5,)  # comma must be present for a single element to identify as a tuple
# print(type(x))

# We can identify the length of a tuple
# print(len(fruit))

# Creating a tuple
# another_tuple = tuple(("Hello", 18, True))  # Double bracket required to create this tuple from other types
# # This tuple was made from a string, integer and boolean
# print(type(another_tuple))

# Converting a tuple to a list then back to a tuple (a loophole to modifying a tuple)
# fruit = list(fruit)
# print(type(fruit))
# fruit.append("pears")
# fruit = tuple(fruit)
# print(fruit)

# Unpacking tuples
# fruit = ("apples", "bananas", "pears", "oranges", "strawberries")
# (one, two, three, four, five) = fruit
# print(one)
# print(four)

# fruit = ("apples", "bananas", "pears", "oranges", "strawberries")
# (one, *two, three) = fruit
# print(one)
# print(tuple(two))  # asterisk used to assign variable to multiple elements from tuple
# print(three)

# Incorporate loops within tuples
# for i in range(len(fruit)):
#     print(fruit[i])
