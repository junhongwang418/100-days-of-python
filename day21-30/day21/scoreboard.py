from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update()

    def increment(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAVE OVER", align="center", font=("Arial", 24, "normal"))
