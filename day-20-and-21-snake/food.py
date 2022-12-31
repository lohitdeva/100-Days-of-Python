import turtle
import random

turtle.register_shape('day-20-and-21-snake/apple.gif')


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shape('day-20-and-21-snake/apple.gif')
        self.color('blue')
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-390, 390), random.randint(-390, 390))