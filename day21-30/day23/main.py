import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.update()

    screen.update()

    if player.check_collision(car_manager.cars):
        break

    if player.check_goal():
        scoreboard.levelup()
        car_manager.speedup()
        player.reset_position()

scoreboard.gameover()

screen.exitonclick()
