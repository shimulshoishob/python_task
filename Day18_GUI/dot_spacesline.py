from turtle import Turtle, Screen

pen = Turtle()
pen.shape("arrow")
pen.color("black")
for i in range(50):
    pen.fd(10)
    pen.penup()
    pen.fd(10)
    pen.pendown()
    pen.right(7)




screen = Screen()
screen.exitonclick()