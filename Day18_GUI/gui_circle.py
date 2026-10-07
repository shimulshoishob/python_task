import random
import turtle
from turtle import Turtle, Screen

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy = Turtle()
turtle.colormode(255) # need for rgb values
timmy.speed("fastest")

def draw_spirograph(gap):
    for i in range(int(360/gap)):
        timmy.circle(150)
        timmy.color(random_color())
        timmy.setheading(timmy.heading()+gap)


draw_spirograph(14)


screen = Screen()
screen.exitonclick()