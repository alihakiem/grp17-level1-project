import turtle
from turtle import Turtle,Screen
turtle1 = Turtle()
turtle1.shape('turtle')
turtle1.speed('slow')
turtle1.fillcolor('green')
turtle1.begin_fill()
for i in range(4):
    turtle1.forward(300)
    turtle1.left(90)
turtle1.end_fill()
turtle1.penup()
turtle1.goto(x =-200,y=100)

turtle1.shape('square')
for i in range(3):
    turtle1.stamp()
    turtle1.forward(100)

turtle1.goto(-100,-100)
turtle1.pendown()
turtle1.circle(50)


print("-----------------------------")
my_screen = Screen()
my_screen.exitonclick()