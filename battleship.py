#!/usr/bin/env python3

import keyboardInput
import display
import time

# emptyBoard = [ [0] * 10 for _ in range(10)]

playerOneTopBoard = [ [0] * 10 for _ in range(10)]
playerOneBottomBoard = [ [0] * 10 for _ in range(10)]
playerTwoTopBoard = [ [0] * 10 for _ in range(10)]
playerTwoBottomBoard = [ [0] * 10 for _ in range(10)]

def getPlayerTurn(counter):
	if turnCounter%2 == 1:
		return "player one"
	else: 
		return "player two"

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

def fireMissile(currboard,aim):
	currboard[aim[0]][aim[1]] = 1
	return currboard

if __name__ == "__main__":
	# every loop in main game loop will refresh the screen 
	# or get keyboard input
	turnCounter = 1

	while True:
		playerTurn = getPlayerTurn(turnCounter)
		if playerTurn == "player one":
			display.playerOneSplash()
			currentTopBoard = playerOneTopBoard
			currentBottomBoard = playerOneBottomBoard
		else:
			display.playerTwoSplash()
			currentTopBoard = playerTwoTopBoard
			currentBottomBoard = playerTwoBottomBoard
		# get keyboard input
		key = keyboardInput.get()
		target = [4,4] # start cursor in center
		display.drawScreen(currentTopBoard,currentBottomBoard,target)
		key = keyboardInput.get()
		while key in ["up","down","left","right"]:
			target = moveTarget(key,target)
			display.drawScreen(currentTopBoard,currentBottomBoard,target)
			key = keyboardInput.get()
		if key == "f": # fired a missile!
			if playerTurn == "player one":
				playerOneTopBoard = fireMissile(playerOneTopBoard,target)
				display.drawScreen(playerOneTopBoard,playerOneBottomBoard,None)
			else: 
				playerTwoTopBoard = fireMissile(playerTwoTopBoard,target)
				display.drawScreen(playerTwoTopBoard,playerTwoBottomBoard,None)

		# update data
		graphicsData = updateData(key)
		# refresh screen
		keyboardInput.get()

		turnCounter += 1
