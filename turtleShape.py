from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
Wyborne = Turtle()
Wyborne.pencolor("blue")
Wyborne.pendown()
Wyborne.pensize(3)

def drawShape(turtle,side,color):
    turtle.pencolor(color)
    drawnSides= 0
    angle= 360/side
    side= s

    while drawnSides < side:
        Wyborne.forward(50)
        Wyborne.right(angle)
        drawnSides+=1

another = True

while another == True:
    print("How many sides?")
    s= input()
    s= int(s)

    print("What color?")
    color= input()

    drawShape(Wyborne,s,color)

    print("Another one?")
    answer = input()
    if (answer == "no"):
        another = False




# Close window on click.
#exitonclick()
