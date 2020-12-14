from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed("fastest")
t.shape("turtle")

num_circles = 30

for _ in range(num_circles):
    t.pencolor((random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)))
    t.circle(50)
    t.right(360 / num_circles)

screen.exitonclick()
