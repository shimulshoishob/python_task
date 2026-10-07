import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def mouse_clicked(x, y):
#     print(x,y)
#
# turtle.onscreenclick(mouse_clicked)

answer = screen.textinput(title="Guess the State", prompt="What is your guess?")

data_file = pandas.read_csv("50_states.csv")
# print(data_file)
print(data_file["states"])
screen.mainloop()