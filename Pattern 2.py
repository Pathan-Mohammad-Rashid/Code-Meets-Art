import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800, startx=0, starty=0)

# Create a turtle for the spiral
spiral = turtle.Turtle()
spiral.speed(1000)

# Create a list of colors
colors = ["red", "orange", "red", "green", "blue", "purple"]

# Draw the spiral
for i in range(500):
    # Change the color of the spiral at random intervals
    if i % 100 == 0:
        spiral.color(random.choice(colors))
    spiral.forward(i)
    spiral.right(91)
