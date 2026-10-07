import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed(0)
screen.listen()
def timmy_forward():
	timmy.forward(100)
def timmy_backward():
	timmy.backward(100)
def timmy_up():
	timmy.left(90)
	timmy.forward(50)
	timmy.right(90)
def timmy_down():
	timmy.right(90)
	timmy.forward(50)
	timmy.left(90)
def timmy_clear():
	timmy.penup()
	timmy.clear()
	timmy.home()
	timmy.pendown()
screen.onkey(key="s", fun=timmy_forward)
screen.onkey(key="a", fun=timmy_backward)
screen.onkey(key="w", fun=timmy_up)
screen.onkey(key="z", fun=timmy_down)
screen.onkey(key="c", fun=timmy_clear)


screen.exitonclick()