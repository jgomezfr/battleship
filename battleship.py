#!/usr/bin/env python3

import keyboardInput
import display

def updateData(keystroke):
	pass

if __name__ == "__main__":
	# every loop in main game loop will refresh the screen 
	# or get keyboard input
	while True:
		# get keyboard input
		key = keyboardInput.get()
		print(key)
		# update data
		graphicsData = updateData(key)
		# refresh screen
		display.drawScreen(graphicsData)
