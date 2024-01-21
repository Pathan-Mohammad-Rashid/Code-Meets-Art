import turtle # import turtle
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100) # setting up the screen
squary = turtle.Turtle()
squary.speed(100)

for i in range(500): #loop 1
  squary.forward(i)
  squary.left(91)


screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)

# Create 1 turtles for 1 spirals
turtles = [turtle.Turtle() for _ in range(1)]

# Set the initial heading for each turtle
for i, t in enumerate(turtles):
    t.speed(10000)
    t.right(i * 90)  # Each turtle faces a different direction (0, 90, 180, 270)

# Draw the spirals
for i in range(500):
    for t in turtles:
        t.forward(i)
        t.right(91)

