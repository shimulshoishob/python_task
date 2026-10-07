import random
from turtle import Turtle, Screen

walk = Turtle()
walk.shape("arrow")
walk.pensize(10)
turtle_colors = [
    "black", "navy", "darkblue", "mediumblue",
    "blue", "darkgreen", "green", "teal",
    "darkcyan", "deepskyblue", "darkturquoise",
    "mediumslateblue", "darkslateblue", "indigo",
    "purple", "darkmagenta", "magenta", "darkviolet",
    "red", "crimson", "firebrick", "orangered",
    "tomato", "coral", "darkorange", "orange",
    "gold", "darkgoldenrod", "yellow", "chartreuse",
    "lime", "limegreen", "springgreen", "mediumseagreen",
    "maroon", "brown", "sienna", "saddlebrown",
    "chocolate", "peru", "darkred", "darksalmon",
    "mediumvioletred", "deeppink", "hotpink", "violet",
    "mediumorchid", "darkorchid", "slateblue", "dodgerblue"
]


walk.speed("fastest")

j=0
while j<200:
    num = random.randint(1,10000)
    walk.color(random.choice(turtle_colors))
    angle = 90*(num%4)
    walk.forward(50)
    walk.right(angle)
    j+=1


screen = Screen()
screen.exitonclick()