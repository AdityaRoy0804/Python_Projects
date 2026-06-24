import turtle
from turtle import Turtle,Screen
import random   

turtle.colormode(255)
turtle.getscreen()

tim = Turtle()
tim.width(2)
tim.speed("fastest")

def random_color():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    color = (r,g,b)
    return color        

while True:
    tim.color(random_color())
    tim.circle(150)
    tim.setheading(tim.heading() + 5)
    if tim.heading() == 360:
        break

screen = Screen()
screen.exitonclick()