from turtle import Turtle
import random

COLORS = ('white','red', 'green')


class Traffic:
    def __init__(self):
        self.cars = []
        if self.cars:
            self.speed = self.cars[0].speed()

    def create_car(self, y_cor):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_len=1)
        car.goto(300, y_cor)
        car.penup()
        car.setheading(180)
        car.speed(1)
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def move_cars(self, speed):
        for cars in self.cars:
            cars.forward(speed)

    def increase_speed(self):
        speed = self.cars[0].speed()
        for cars in self.cars:
            cars.speed(speed + 1)


