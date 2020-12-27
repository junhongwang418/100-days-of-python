from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def check_collision(self, cars):
        for c in cars:
            if abs(c.xcor() - self.xcor()) <= 28 and abs(c.ycor() - self.ycor()) <= 18:
                return True

        return False

    def check_goal(self):
        return self.ycor() >= 280

    def reset_position(self):
        self.goto(STARTING_POSITION)
