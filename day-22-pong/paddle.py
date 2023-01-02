from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        '''
        Accepts a position as an input and creates a paddle object
        at that position
        '''
        super().__init__()
        self.shape('square')
        self.speed(0)
        self.setheading(90)
        self.color('#ffffff')
        self.shapesize(stretch_wid=None, stretch_len=5)
        self.up()
        self.goto(position)

    def move_up(self):
        '''
        Moves the paddle up
        '''
        if self.ycor() >= 290:
            return
        self.fd(20)

    def move_down(self):
        '''
        Moves the paddle down
        '''
        if self.ycor() <= -290:
            return
        self.bk(20)