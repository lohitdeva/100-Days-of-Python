from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake_body = list()
s = Screen()

s.setup(width=800, height=800)
s.colormode(255)
s.bgcolor('black')
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.update()

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    s.listen()
    s.onkeypress(key='Up', fun=snake.up)
    s.onkeypress(key='Down', fun=snake.down)
    s.onkeypress(key='Left', fun=snake.left)
    s.onkeypress(key='Right', fun=snake.right)

    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.increase_score()

    if abs(snake.head.xcor()) > 390 or abs(
            snake.head.ycor()) > 390 or snake.snake_collide():
        scoreboard.game_over()
        s.update()
        game_is_on = False

s.exitonclick()
