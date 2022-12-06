import turtle

# Set the turtle's speed to the maximum possible value
turtle.speed(0)

# Set the background color
turtle.bgcolor("white")

# Set the turtle's pen size
turtle.pensize(2)

# Define a function for drawing a Sierpinski triangle
def sierpinski(length, depth):
    if depth == 0:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# Move the turtle to the center of the screen
turtle.penup()
turtle.setposition(-200, -100)
turtle.pendown()

# Draw the Sierpinski triangle
sierpinski(400, 6)

# Prevent the turtle window from closing automatically
turtle.mainloop()
