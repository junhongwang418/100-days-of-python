from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.shape("turtle")
t.pensize(10)
t.speed("fastest")

while True:
    num_turns = random.randint(0, 3)
    t.right(90 * num_turns)
    t.pencolor((random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)))
    t.forward(20)
