import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 500, startx=0, starty=0)

# Create a turtle for the pattern
pattern = turtle.Turtle()
pattern.speed(100000000000)

# Create a list of colors
colors = ["blue","red", "black"]

# Function to draw a square
def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(turtle, size):
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)

# Draw the pattern
for i in range(10000):
    # Change the color at random intervals
    pattern.color(random.choice(colors))
    # draw_square(pattern, i*2)
    draw_triangle(pattern, i*2)
    pattern.right(100)
