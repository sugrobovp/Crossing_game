from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.color('white')
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)


