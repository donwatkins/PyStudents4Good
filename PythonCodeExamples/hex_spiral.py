import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed to the maximum possible value
t.speed(0)

# Set the turtle's pen size to a larger value to make the lines more visible
t.pensize(2)

# Set the turtle's pen color to blue
t.pencolor("blue")

# Set the turtle's starting position
t.penup()
t.setpos(-100, 0)
t.pendown()

# Draw the spiral
for i in range(100):
    t.circle(i, 60)

# Keep the window open until the user closes it
turtle.done()
