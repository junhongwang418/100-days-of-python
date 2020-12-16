from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100+i*50)
    turtles.append(t)

done = False

while not done:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            win_color = turtle.pencolor()
            done = True
            break

if user_bet == win_color:
    print(f'You win! Turtle with color {win_color} won.')
else:
    print(f'You lost! Turtle with color {win_color} won.')

screen.exitonclick()
