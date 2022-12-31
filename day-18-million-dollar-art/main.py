# Python script to analyse an image of a Damien Hirst dot painting,
# extract its color pallette and recreate an art piece of the same
# style using the same pallette
#
# Created by: Lohit Deva
# 30/12/2022

import colorgram
from turtle import Turtle, Screen
import random

# colorgram extracts colors from a specified image and returns them as a list of rgb objects
colors = colorgram.extract('day-18-million-dollar-art/image.jpg', 30)

colors_list = list()
for color in colors:
    # Exclude shades of gray beyond rgb(180, 180, 180)
    if color.rgb.r > 180 and color.rgb.g > 180 and color.rgb.b > 180:
        continue
    colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

turtle = Turtle()
screen = Screen()

dot_size = 20
space_size = 50
rows = 10
columns = 10

# Dynamically calculate canvas size based on requirements
canvas_width = ((dot_size + space_size) * columns) + (3 * space_size)
canvas_height = ((dot_size + space_size) * rows) + (3 * space_size)
screen.setup(width=canvas_width + space_size,
             height=canvas_height + space_size)
screen.screensize(canvwidth=canvas_width, canvheight=canvas_height)
screen.colormode(255)

# Set start point of turtle as bottom left corner of screen
origin_x = (canvas_width / 2) - (space_size + dot_size)
origin_y = (canvas_height / 2) - (space_size + dot_size)

turtle.up()
turtle.hideturtle()
turtle.goto(-(origin_x), -(origin_y))

turtle.speed(0)

for i in range(rows):
    for j in range(columns):
        color = random.choice(colors_list)
        turtle.color(color)
        turtle.dot(dot_size)
        turtle.fd((dot_size * 2) + space_size)
    turtle.goto(-(origin_x), turtle.ycor() + (dot_size + space_size))

screen.exitonclick()