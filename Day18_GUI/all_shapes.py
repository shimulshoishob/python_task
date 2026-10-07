from turtle import Turtle, Screen
import random

arrow = Turtle()
arrow.shape("arrow")
colors = [
    "navy", "cyan", "magenta", "lime green", "dark red", "dark blue", "red",
    "dark magenta", "chartreuse", "black", "white", "silver", "gray", "maroon",
    "purple", "fuchsia", "green", "lime", "olive", "yellow", "teal", "aqua",
    "blue", "orange", "pink", "brown", "beige", "ivory", "gold", "coral",
    "salmon", "crimson", "indigo", "violet", "lavender", "plum", "turquoise",
    "azure", "mint", "peach", "wheat", "khaki", "tan", "chocolate", "orchid",
    "thistle", "sky blue", "steel blue", "olive drab", "forest green",
    "sea green", "dark green", "medium blue", "midnight blue", "dodger blue",
    "cornflower blue", "royal blue", "powder blue", "light blue", "pale green",
    "spring green", "medium sea green", "light sea green", "dark slate gray",
    "slate gray", "light slate gray", "dark cyan", "light cyan",
    "dark turquoise", "medium turquoise", "pale turquoise", "aquamarine",
    "medium aquamarine", "dark olive green", "dark sea green", "light green",
    "dark slate blue", "medium slate blue", "medium purple", "dark orchid",
    "medium orchid", "rosy brown", "sandy brown", "goldenrod", "dark goldenrod",
    "peru", "burlywood", "bisque", "blanched almond", "moccasin",
    "navajo white", "papaya whip", "misty rose", "lavender blush", "linen",
    "old lace", "seashell", "snow", "honeydew", "mint cream", "alice blue",
    "ghost white", "floral white", "antique white", "lemon chiffon",
    "cornsilk", "light goldenrod yellow", "dark khaki", "pale goldenrod",
    "green yellow", "dark salmon", "light salmon", "tomato", "hot pink",
    "deep pink", "pale violet red", "medium violet red", "firebrick",
    "dark orange", "light coral", "cadet blue", "dark slate grey", "dim gray",
    "slate blue", "medium spring green"
]

for i in range(3,100):
    arrow.color(random.choice(colors))
    for j in range(i):
        arrow.fd(100)
        arrow.left(360/i)


screen = Screen()
screen.exitonclick()