import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
turtle.getscreen()

tim = Turtle()
tim.shape("turtle")
tim.width(10)
tim.speed(random.randrange(1,10))

for _ in range(100):
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    tim.color(r,g,b)
    tim.forward(random.randrange(30,100))
    tim.setheading(random.choice([0,90,180,270]))

screen = Screen()
screen.exitonclick()

