from turtle import Turtle, Screen
import random

s = Screen()

s.setup(width=1000, height=800)
s.bgpic('day-19/background.gif')
s.title('Turtle GP 2022')

user_bet = s.textinput(
    title='Make your bet',
    prompt=
    'Which turtle will win the race? Enter a color:\n\n(red/orange/yellow/green/blue/purple)'
).strip().lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while user_bet not in colors:
    user_bet = s.textinput(
        title='Wrong choice',
        prompt='That color does not exist, please try again:')

turtle_list = list()
is_race_on = False

for i in range(1, 7):
    turtle = Turtle(shape="turtle")
    turtle.resizemode('user')
    turtle.shapesize(stretch_wid=2, stretch_len=2, outline=2)
    eval('turtle.color("' + colors[i - 1] + '")')
    eval('turtle.up()')
    y_cor = (i * 80) - 270
    eval('turtle.goto(x=-460, y=' + str(y_cor) + ')')
    turtle.speed('fastest')
    turtle_list.append(turtle)

if user_bet and user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 420:
            is_race_on = False
            winner = turtle.pencolor()
            break

print(f"The winner is '{winner}'")
if winner == user_bet:
    print("You win! 💲💲💲")
else:
    print("You lose! 😥😭😞")

s.exitonclick()
