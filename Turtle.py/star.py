import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
turtle.getscreen()

tim = Turtle()
tim.shape("turtle")
tim.width(1)
tim.color("red","yellow")
tim.speed(6)   
tim.begin_fill()
while True:
    tim.forward(250)
    tim.left(175)
    if tim.heading() == 0:
        break

tim.end_fill()

screen = Screen()
screen.exitonclick()