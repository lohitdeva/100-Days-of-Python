# For this project, refer to the website - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#
# Here, the aim is to help the robot 'Reeborg' escape a randomly generated maze using some pre-defined functions from within the Reeborg library and python concepts such as if-else blocks, while loops and creating functions.

#
# The pre-defined functions used here are turn_left(), at_goal(), right_is_clear(), front_is_clear, and move().

# Created by: Lohit Deva
# 10/12/2022

# NOTE: This code will not execute on its own and can only be run at the URL specified above

# This loop is to make the robot continue in a straight path until it encounters a wall
while front_is_clear():
	move()

# After the robot hits a wall, it turns left so that it can continue to follow the right side of the maze
turn_left()

# This function turns the robot right as there no pre-defined function to achieve this
def turn_right():
	for i in range(3):
	turn_left()

# at_goal() evaluates to true once the robot reaches the end of the maze
while not at_goal():

	# Here the robot takes the opportunity to turn right if possible.
	if right_is_clear():
		turn_right()
		move()
	
	# If it cannot go right, the robot will continue to move straight.
	elif front_is_clear():
		move()

	# If the robot cannot go straight or left, it will turn left.
	else:
		turn_left()
