# Creating drawings using the package "Turtle"

# Import Turtle
import turtle

# Get a set-up in Turtle
turtle.bgcolor("black")  # Background colour
turtle.pensize(2)  # Pen size
turtle.color("red")
turtle.speed(0)

# # Draw a square
# turtle.forward(50)  # Moves forward
# turtle.left(90)  # Turns 90 degrees anticlockwise
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # Allows turtle to stay on screen


# Little project in turtle - creates a nice drawing
# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# Let's make it more complex
for i in range(30):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(2)
turtle.done()
