from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        '''
        Creates a scoreboard object that creates two variables to hold the scores and writes
        them to the screen.
        '''
        super().__init__()
        self.color('#ffffff')
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 240)
        self.write_score()

    def increase_score(self, side):
        '''
        Accepts a side (str) as input and increases the score for that side.
        '''
        if side == 'left':
            self.l_score += 1
        else:
            self.r_score += 1
        self.write_score()

    def write_score(self):
        '''
        Clears any score written on the screen and rewrites the current scores.
        '''
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score,
                   align='center',
                   font=('Courier', 80, 'normal'))
        self.goto(100, 240)
        self.write(self.r_score,
                   align='center',
                   font=('Courier', 80, 'normal'))