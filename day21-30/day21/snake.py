from turtle import Screen, Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.turtles = []

        for i in range(3):
            t = Turtle("square")
            t.penup()
            t.goto(i * -20, 0)
            t.color("white")
            self.turtles.append(t)

        self.head = self.turtles[0]

    def move(self):
        """Move the head forward. The tail follows the head."""
        for i in range(len(self.turtles) - 1, 0, -1):
            turtle_front = self.turtles[i - 1]
            self.turtles[i].goto(turtle_front.xcor(), turtle_front.ycor())
        self.head.forward(20)

    def extend(self):
        t = Turtle("square")
        t.penup()
        t.goto(self.turtles[-1].position())
        t.color("white")
        self.turtles.append(t)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
