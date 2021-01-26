# Functions in Python

# A function takes an argument and produces a result

# The general form of a function in Python is:
# def function_name(arguments):
#   {lines telling the function what to do to produce the result}
#   return result


# Let's consider producing a function that returns x^2 + y^2
# def squared(x, y):
#     result = x**2 + y**2
#     return result
#
#
# print(squared(10, 2))


# Function for country of birth
def birthplace(country):
    return print("I am from", country)


birthplace("England")