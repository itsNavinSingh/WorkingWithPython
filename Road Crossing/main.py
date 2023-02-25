import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
def game_is_off():
    global game_is_on
    game_is_on = False
while game_is_on:
    car_manager.move_car()
    time.sleep(0.1)
    if random.randint(1, 6) == 6:
        car_manager.create_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_off()
            score.game_over()
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()
    screen.update()
screen.exitonclick()
