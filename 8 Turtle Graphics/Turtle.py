### Copyright Adren Poulard

## You will now learn how to use Turtle Graphics in Python

## Example for making a red square filled in yellow
# Always make sure to import the turtle module or it won't work!
import turtle
from turtle import *

# Make the turtle go forward
def straight():
    turtle.forward(50)

# Make the turtle turn right    
def turn_right():
    turtle.right(90)

# Choose colors (outline, fill)
color('red', 'yellow')
begin_fill()

# Call functions
while True:
    straight()
    turn_right()

    # If turtle returns to starting point, stop
    if abs(pos()) < 1:
        break

#Stop colors
end_fill()
done()

# Now draw a flag (you can erase the code for creating a square)
