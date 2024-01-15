import random
from turtle import Turtle,Screen
turtle1 =Turtle()
colors_list = ['red','green','blue','black','gray','brown']

turtle1.speed('fastest')
for i in range(25):
    chosen_color = random.choice(colors_list)
    turtle1.color(chosen_color)
    turtle1.circle(100)
    turtle1.left(15)




my_screen = Screen()
my_screen.exitonclick()