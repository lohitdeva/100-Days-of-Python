import turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.register_shape('day-20-and-21-snake/snake-head/snake-head-down.gif')
turtle.register_shape('day-20-and-21-snake/snake-head/snake-head-left.gif')
turtle.register_shape('day-20-and-21-snake/snake-head/snake-head-right.gif')
turtle.register_shape('day-20-and-21-snake/snake-head/snake-head-up.gif')


class Snake:

    def __init__(self):
        self.snake_body = list()

        for i in range(3):
            snake_part = self.create_part()
            snake_part.goto(x=(-(MOVE_DISTANCE) * i), y=0)
            self.snake_body.append(snake_part)

        self.head = self.snake_body[0]
        self.head.shape('day-20-and-21-snake/snake-head/snake-head-right.gif')
        self.tail = self.snake_body[len(self.snake_body) - 1]

    def create_part(self):
        snake_part = turtle.Turtle()
        snake_part.speed('fastest')
        snake_part.shape('square')
        snake_part.fillcolor(205, 220, 57)
        snake_part.up()
        return snake_part

    def extend_snake(self):
        snake_part = self.create_part()
        snake_part.goto(self.tail.position())
        self.snake_body.append(snake_part)

    def snake_collide(self):
        for snake_part in self.snake_body[1:]:
            if self.head.distance(snake_part) < 15:
                return True

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(x=self.snake_body[i - 1].xcor(),
                                    y=self.snake_body[i - 1].ycor())
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.shape('day-20-and-21-snake/snake-head/snake-head-up.gif')

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.shape(
                'day-20-and-21-snake/snake-head/snake-head-down.gif')

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.shape(
                'day-20-and-21-snake/snake-head/snake-head-left.gif')

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
            self.head.shape(
                'day-20-and-21-snake/snake-head/snake-head-right.gif')
