from turtle import Turtle

UP_AND_RIGHT = 45
UP_AND_LEFT = 135
DOWN_AND_LEFT = 225
DOWN_AND_RIGHT = 315


class Ball(Turtle):

    def __init__(self):
        '''
        Creates a ball that moves up and to the right
        '''
        super().__init__()
        self.shape('circle')
        self.color('#ffffff')
        self.up()
        self.setheading(UP_AND_RIGHT)
        self.speed('slowest')

    def move_ball(self):
        '''
        Moves the ball in its current direction by 2 places
        '''
        self.fd(2)

    def bounce_wall(self):
        '''
        Bounces the ball off a wall by changing its direction accordingly
        '''
        if self.heading() == UP_AND_RIGHT:
            self.setheading(DOWN_AND_RIGHT)
        elif self.heading() == DOWN_AND_RIGHT:
            self.setheading(UP_AND_RIGHT)
        elif self.heading() == UP_AND_LEFT:
            self.setheading(DOWN_AND_LEFT)
        else:
            self.setheading(UP_AND_LEFT)

    def paddle_bounce(self):
        '''
        Bounces the ball off a paddle by changing its direction accordingly
        '''
        self.setheading((self.heading() + 180) % 360)

    def ball_reset(self, direction):
        '''
        Resets the ball and its trajectory to its original values
        '''
        self.goto(x=0, y=0)
        eval('self.setheading(UP_AND_' + direction.upper() + ')')
