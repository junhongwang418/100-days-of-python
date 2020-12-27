from turtle import Turtle

SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("white")
        self.vx = SPEED
        self.vy = SPEED

    def update(self):
        self.setpos((self.xcor() + self.vx, self.ycor() + self.vy))

    def bounce_x(self):
        self.vx *= -1
        self.speedup()

    def bounce_y(self):
        self.vy *= -1
        self.speedup()

    def restart(self):
        self.goto((0, 0))
        self.bounce_x()
        self.vx = SPEED if self.vx > 0 else -SPEED
        self.vy = SPEED if self.vy > 0 else -SPEED

    def speedup(self):
        self.vx *= 1.1
        self.vy *= 1.1
