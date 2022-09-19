from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.color('white')
        self.penup()
        self.goto(-260, 260)
        self.next_level()

    def next_level(self):
        self.clear()
        self.level += 1
        text = 'Level: {0}'.format(self.level)
        self.write(text)


