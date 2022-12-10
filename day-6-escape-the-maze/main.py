# For this project, refer to the website - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#
# Here, the aim is to help the robot 'Reeborg' escape a randomly generated maze using some pre-defined functions from within the Reeborg library and python concepts such as if-else blocks, while loops and creating functions.

#
# The pre-defined functions used here are turn_left(), at_goal(), right_is_clear(), front_is_clear, and move().

# Created by: Lohit Deva
# 10/12/2022

# NOTE: This code will not execute on its own and can only be run at the URL specified above

# This function turns the robot right as there no pre-defined function to achieve this
def turn_right():
	for i in range(3):
	turn_left()

# at_goal() evaluates to true once the robot reaches the end of the maze
while not at_goal():

	# If both front and right is clear, the robot should move straight ahead. Otherwise it gets stuck in
	# an infinite loop of turning right
	if right_is_clear() and front_is_clear():
		move()
	
	# Here, the robot takes the opportunity to turn right if it see the opportunity
	elif right_is_clear():
		turn_right()
		move()
	
	# Here the robot continues to move along the right edge of the maze
	elif front_is_clear():
		move()
	
	# Here the robot turns left if it is unable to proceed straight or turn right
	else:
		turn_left()
