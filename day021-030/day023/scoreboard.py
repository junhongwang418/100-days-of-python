from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)

    def levelup(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
