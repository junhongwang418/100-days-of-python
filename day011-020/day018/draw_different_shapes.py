from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")

for num_points in range(3, 9):
    for _ in range(num_points):
        t.forward(100)
        t.right(360 / num_points)

screen = Screen()
screen.exitonclick()
