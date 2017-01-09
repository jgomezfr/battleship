#!/usr/bin/env python3

import getch

def getInput():
	return getch.getinput()

def updateData(keystroke):
	pass

def display(graphicsData):
	pass

if __name__ == "__main__":
	# every loop in main game loop will refresh the screen 
	# or get keyboard input
	while True:
		# get keyboard input
		keystroke = getInput()
		print(keystroke)
		# update data
		graphicsData = updateData(keystroke)
		# refresh screen
		display(graphicsData)
