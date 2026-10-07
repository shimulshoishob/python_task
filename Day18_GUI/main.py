from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")
tim.pencolor("black")
for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()