from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

        for i in range(30):
            t = Turtle(shape="square")
            t.penup()
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.goto(320 + i * 20, random.randint(-260, 260))
            self.cars.append(t)

    def update(self):
        for t in self.cars:
            t.goto(t.xcor() - self.speed, t.ycor())
            if t.xcor() < -320:
                t.goto(320, random.randint(-260, 260))

    def speedup(self):
        self.speed += MOVE_INCREMENT
