import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
Scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

car = CarManager()

game_is_on = True
refresh_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    
    refresh_counter += 1
    if refresh_counter % 10 == 0:
        car.create()

    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            Scoreboard.game_over()
            screen.update()
            time.sleep(5)
            game_is_on = False
            break 
    
    if player.is_at_finish_line():
        player.go_to_start()
        car.increase_speed()
        Scoreboard.next_level()

    
