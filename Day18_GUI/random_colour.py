import random
import turtle
from turtle import Turtle, Screen
from gui_circle import random_color

timmy = Turtle()
turtle.colormode(255)

timmy.shape("classic")

timmy_angle = [0, 90, 180, 270]
for i in range(100):
    timmy.pensize(random.randint(1, 5))
    timmy.color(random_color())
    timmy.color(random_color())
    timmy.fd(30)
    timmy.right(random.choice(timmy_angle))
    timmy.pencolor(random_color())



screen = Screen()
screen.exitonclick()