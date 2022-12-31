from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Calibri', 20, 'normal')
FONT_COLOR = 'white'


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.up()
        self.goto(0, 360)
        self.hideturtle()
        self.color(FONT_COLOR)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'Game over', align=ALIGNMENT, font=FONT)
