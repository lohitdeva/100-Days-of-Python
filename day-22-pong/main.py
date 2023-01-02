from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def reset_paddle(paddle):
    '''
    Accepts a paddle object as input and restores it to its inital position
    '''
    if paddle.xcor() < 0:
        paddle.goto(-600, 0)
    else:
        paddle.goto(600, 0)


t = Turtle()
s = Screen()

# Setting up the game window
s.setup(width=1280, height=720)
s.colormode(255)
s.bgcolor('#000000')
s.title("Pong")
s.tracer(0)

# Setting up the game elements
left_paddle = Paddle((-600, 0))
right_paddle = Paddle((600, 0))
ball = Ball()
sb = Scoreboard()

# Setting up a turtle that will draw the center line
t.color('#ffffff')
t.hideturtle()
t.speed(0)

t.setheading(90)
t.up()
t.goto(x=0, y=350)
t.setheading(270)

t.width(10)
t.down()

# Drawing the center line
for _ in range(14):
    t.fd(10)
    t.up()
    t.fd(30)
    t.down()
    t.fd(10)

t.up()
s.update()
continue_game = True

# Start of the actual game
while continue_game:
    s.update()
    s.listen()
    ball.move_ball()
    s.onkeypress(key='w', fun=left_paddle.move_up)
    s.onkeypress(key='s', fun=left_paddle.move_down)
    s.onkeypress(key='Up', fun=right_paddle.move_up)
    s.onkeypress(key='Down', fun=right_paddle.move_down)

    # Detecting wall collision
    if abs(ball.ycor()) >= 330:
        ball.bounce_wall()

    # Detecting paddle collision
    if (ball.distance(right_paddle) < 50
            or ball.distance(left_paddle) < 50) and abs(ball.xcor()) > 590:
        ball.paddle_bounce()

    # Detecting ball going out of bounds and updating score as well as resetting paddles and ball
    if abs(ball.xcor()) > 650:
        if ball.xcor() > 650:
            ball.ball_reset('right')
            sb.increase_score('left')
        else:
            ball.ball_reset('left')
            sb.increase_score('right')
        reset_paddle(left_paddle)
        reset_paddle(right_paddle)
        time.sleep(0.5)

    # Ending the game if any player reaches a score of 5 and declaring them the winner
    if sb.l_score == 5:
        t.goto(x=-150, y=-20)
        t.write("Player 1 wins",
                align='center',
                font=('Courier', 20, 'normal'))
        continue_game = False
    elif sb.r_score == 5:
        t.goto(x=150, y=-20)
        t.write("Player 2 wins",
                align='center',
                font=('Courier', 20, 'normal'))
        continue_game = False

s.exitonclick()