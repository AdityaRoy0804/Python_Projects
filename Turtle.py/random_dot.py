import turtle
import random
from turtle import Turtle,Screen    

turtle.colormode(255)
turtle.getscreen()  

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

def random_color():
    r = random.randrange(0,255)    
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    color = (r,g,b)
    return color
    
for _ in range(100):
    tim.color(random_color())
    tim.dot(20)
    tim.goto(random.randrange(-250,250),random.randrange(-250,250))

    
screen = Screen()
screen.exitonclick()