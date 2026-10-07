# import colorgram
#
# colors = colorgram.extract('shoishob_colorgram.jpg', 30)
#
# color_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)
#  above code use to extract colours
import turtle
import random
from turtle import Turtle

from turtle import Screen

color_list = [
    (244, 242, 238), (124, 181, 211), (199, 174, 15), (247, 226, 234), (222, 232, 240), (26, 121, 168), (178, 13, 44),
    (237, 204, 87), (239, 148, 73), (220, 122, 162), (232, 241, 235), (25, 144, 72), (216, 80, 124), (7, 172, 211),
    (214, 59, 26), (66, 21, 54), (239, 77, 44), (247, 156, 189), (8, 184, 151), (161, 56, 107), (10, 30, 72),
    (74, 28, 23),
    (128, 208, 234), (13, 48, 132), (167, 193, 164), (101, 116, 184), (252, 156, 151), (167, 24, 19), (3, 88, 57),
    (111, 217, 215)
]

timmy = Turtle()
timmy.penup()
timmy.hideturtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.setx(-400)
timmy.sety(-400)
timmy.color("black")
print(timmy.heading())
for i in range(10):
    for j in range(10):
        timmy.fd(50)
        timmy.pendown()
        x = random.choice(color_list)
        timmy.pencolor(x)
        timmy.dot(20,x)
        timmy.penup()
    timmy.setx(-300)
    timmy.sety((-300)+50*(i+1))

screen = Screen()
screen.exitonclick()
