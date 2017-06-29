#importing libraries
from turtle import*
import math

#setting up screen size
setup(500,500)

#FUNCTIONS
def whileDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawSides = 0
    angle = 360/sides
    
    while drawSides < sides:
        turtle.forward(60)
        turtle.right(angle)
        drawSides +=1

def forDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    angle = 360/sides

    for s in range(sides):
        turtle.forward(60)
        turtle.right(angle)
        
            
    

#RUNNING CODE
lance = Turtle() #creates turtle
lance.turtlesize(2,2) #makes turtle larger
lance.pensize(5)#makes pen larger
lance.pendown()

another = True

while another == True:
    print("How many sides?")
    sides= int(input())

    print("What color?")
    color= input()

    forDrawShape(lance,sides,color)
    
    print("Another?")
    answer= input()
    
    if (answer == "no"):
        another = False



#closes the turtle window on click
exitonclick()
