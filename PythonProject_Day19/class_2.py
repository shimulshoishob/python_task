import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)

race = False
user_input = screen.textinput(title="predict which colour turtle may win?",prompt="Enter color(red/green/blue/lime/purple/cyan)):").lower()
if user_input:
	race = True

colors = ['red', 'green', 'blue', 'lime', 'purple', 'cyan']
win_line = Turtle()
win_line.hideturtle()
win_line.color("black")
win_line.penup()
win_line.goto(220,-200)
win_line.pendown()
win_line.lt(90)
win_line.fd(400)


turtle_object = []
for i in range(6):
	new_turtle = Turtle()
	new_turtle.shape("turtle")
	new_turtle.speed("slow")
	new_turtle.penup()
	new_turtle.color(colors[i])
	new_turtle.goto(-240, 200 - (i + 1) * 50)
	turtle_object.append(new_turtle)

win_color =""
while race:
	for turtle in turtle_object:
		rand_num = random.randint(5,10)
		turtle.forward(rand_num)
		if turtle.xcor() > 225:
			win_color = turtle.pencolor()
			race = False

if win_color == user_input:
	print(f"You win!{win_color}")
else:
	print(f"You lose! win:{win_color}")

screen.exitonclick()
