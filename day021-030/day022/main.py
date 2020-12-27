from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_r = Paddle(x=350, y=0)
paddle_l = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

done = False

while not done:
    screen.update()
    ball.update()

    # collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    if (ball.distance(paddle_r) < 53 and ball.xcor() > 330) or (ball.distance(paddle_l) < 53 and ball.xcor() < -330):
        ball.bounce_x()

    # collision with right wall
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.increment_score_l()
    # collision with left wall
    elif ball.xcor() < -380:
        ball.restart()
        scoreboard.increment_score_r()


screen.exitonclick()
