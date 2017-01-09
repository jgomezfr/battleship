#!/usr/bin/env python3

import keyboardInput
import display

emptyBoard = [ [0] * 10 for _ in range(10)]

playerOneTopBoard = emptyBoard
playerOneBottomBoard = emptyBoard
playerTwoTopBoard = emptyBoard
playerTwoBottomBoard = emptyBoard

def updateData(keystroke):
	pass

if __name__ == "__main__":
	# every loop in main game loop will refresh the screen 
	# or get keyboard input
	turnCounter = 1

	while True:
		if turnCounter%2 == 1:
			display.playerOneSplash()
		else:
			display.playerTwoSplash()
		# get keyboard input
		key = keyboardInput.get()
		
		# update data
		graphicsData = updateData(key)
		# refresh screen
		display.drawScreen(emptyBoard,emptyBoard)
		keyboardInput.get()

		turnCounter += 1
