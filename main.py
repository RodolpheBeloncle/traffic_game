import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

traffic = CarManager()
traffic.hideturtle()
level = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.build_car()
    traffic.move_cars()


    if player.level_up() == True:
        level.next_level()
        player.reset_position()

# Detect collision with car:
    for car in traffic.traffic_car:
        if car.distance(player) < 20:

            game_is_on = level.game_over()


screen.exitonclick()




