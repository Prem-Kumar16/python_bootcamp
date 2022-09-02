import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_is_on = True
loop_no = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create car for every 6th loop time to reduce traffic
    if loop_no % 6 == 0:
        car.create_car()
    car.move_cars()
    # Detect collision with car
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect level finish
    if player.reached():
        player.goto_start()
        car.level_up()
        scoreboard.new_level()
    loop_no += 1


screen.exitonclick()
