#Importing the relevant modules
import matplotlib.pyplot as plt

# Plotting graphs in Python

# Basic plot
# x = [1, 4, 8, 11]  # This is what we are plotting
# plt.plot(x)
# plt.show()  # This will show the plot


# Plotting two lists against each other - example: age vs average shoe size (UK edition)
# x = [1, 6, 12, 22, 35]  # Age
# y = [1, 4, 8, 11, 11]  # Average shoe size
# plt.plot(x, y)
# plt.show()


# Let's plot something more advanced

# Line 1 - points
x = [3, 9, 14]
y = [2, 7, 30]

# Plotting x and y
plt.plot(x, y, c="red", linewidth=2, label="Solid, no points")

# Line 2 - points
x2 = [1, 15, 18]
y2 = [1, 3, 12]

# Plotting x2 and y2
plt.plot(x2, y2, c="blue", linewidth=2, label="Dashed, points shown", linestyle="dashed",
         marker="o", markerfacecolor="purple", markersize=10)

# Label the axes and give the plot a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2 lines")

# Axes limits
plt.xlim(0, 20)
plt.ylim(0, 40)

# Show the legend on the plot
plt.legend()

# Get Python to show the plot
plt.show()
