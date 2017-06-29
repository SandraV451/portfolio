#importing libraries
from turtle import*
import math

#setting up screen size
setup(500,500)


#Function
def whileDrawHouse(turtle,sides,color):
    turtle.pencolor(color)
    drawsides = 0
    angle = 360/sides

    while drawsides < sides:
        turtle.forward(60)
        turtle.right(angle)
        drawsides +=1

def forTriangle(turtle,sides,color):
    turtle.pencolor
    drawsides = 0
    angle = 360/sides

    while drawsides < sides:
        turtle.forward(60)
        turtle.left(angle)
        drawsides +=1
        

#RunningCode
keith = Turtle()
keith.pensize(4)
keith.turtlesize(2,2)
keith.pendown()

another = True

while another == True:
    print("Want a house?")
    answer= input()

    print("What color?")
    color= input()

    whileDrawHouse(keith,4,color)
    forTriangle(keith,3,color)

    print("Another?")
    answer= input()

    if (answer == "no"):
         another = False
    elif (answer == "yes"):
        keith.penup()
        keith.forward(90)
        keith.pendown()
        another = True
        

#close
exitonclick()
    
