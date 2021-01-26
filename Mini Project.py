# Weighted Module Score Average

# Entering how many modules have been done
number_of_modules = int(input("Enter number of modules: "))

# Entering how many credits these exams cover
total_credits = int(input("Enter how many credits these modules cover: "))

# Begin with average of 0 and then add up percentages from each module
average = 0
for module in range(number_of_modules):
    percentage = int(input("Enter an module score: "))
    module_credits = int(input("Enter this module's credits: "))
    average = average + ((percentage * module_credits) / total_credits)
print("Your average is", average)
