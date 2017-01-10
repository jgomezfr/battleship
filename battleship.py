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

def moveTarget(keystroke,cursor):
	if keystroke == "up":
		if cursor[0]>0:
			cursor[0]-=1
		else:
			pass
	elif keystroke == "down":
		if cursor[0]<9:
			cursor[0]+=1
		else:
			pass
	elif keystroke == "left":
		if cursor[1]>0:
			cursor[1]-=1
		else:
			pass
	elif keystroke == "right":
		if cursor[1]<9:
			cursor[1]+=1
		else:
			pass
	else:
		print("bad keystroke!")
	return cursor

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
		target = [4,4]
		display.drawScreen(emptyBoard,emptyBoard,target)
		key = keyboardInput.get()
		while key in ["up","down","left","right"]:
			target = moveTarget(key,target)
			display.drawScreen(emptyBoard,emptyBoard,target)
			key = keyboardInput.get()
		# update data
		graphicsData = updateData(key)
		# refresh screen
		keyboardInput.get()

		turnCounter += 1
