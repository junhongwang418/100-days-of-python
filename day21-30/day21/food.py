from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Go to random location on the screen."""
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
