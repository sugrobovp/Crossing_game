import random
from turtle import Screen, Turtle
from player import Player
from traffic import Traffic
import time
from level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Turtle crossing')
screen.tracer(0)

player = Player()
traffic = Traffic()
level = Level()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


def game_over():
    segment = Turtle(visible=False)
    segment.goto(-60, 0)
    segment.color('red')
    segment.write('Game over', align='left', font=('Arial', 20, 'normal'))


speed = 5
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    random_line = random.randrange(-240, 240, 20)
    traffic.create_car(random_line)
    traffic.move_cars(speed)
    for car in traffic.cars:
        if player.distance(car) < 5:
            game_is_on = False
            game_over()
    if player.pos()[1] >= 280:
        speed += 1
        level.next_level()
        player.goto(0, -280)


screen.exitonclick()
