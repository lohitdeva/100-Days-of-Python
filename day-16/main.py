# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink","CornflowerBlue")

# timmy.begin_fill()
# for _ in range(4):
#     timmy.fd(100)
#     timmy.lt(90)
# timmy.end_fill()

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)