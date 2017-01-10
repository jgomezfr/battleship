#!/usr/bin/env python3

import keyboardInput
import display
import time
import random

# emptyBoard = [ [0] * 10 for _ in range(10)]

playerOneTopBoard = [ [0] * 10 for _ in range(10)]
playerOneBottomBoard = [ [0] * 10 for _ in range(10)]
playerTwoTopBoard = [ [0] * 10 for _ in range(10)]
playerTwoBottomBoard = [ [0] * 10 for _ in range(10)]

def checkCollisions(piece):
	pass

def addPieceToBoard(board,pieceLocation):
	for location in pieceLocation:
		for row in range(len(board)):
			for col in range(len(board[0])):
				if location[0]==row and location[1]==col:
					board[row][col]=1
				else:
					pass

def placePieces(playerOne,playerTwo):
	for player in range(1,3):
		allShips = ["carrier","battleship","cruiser","submarine","destroyer"]
		allSizes = [5,4,3,3,2]
		orientations = ["vertical","horizontal"]
		for i in range(len(allShips)):
			shipName = allShips[i]
			shipSize = allSizes[i]
			piecePlaced = False
			while piecePlaced == False:
				# try to place piece
				startRow = random.randint(0,9)
				startCol = random.randint(0,9)
				orientation = orientations[random.randint(0,1)]
				pieceLocation = [[startRow,startCol]]
				currRow = startRow
				currCol = startCol
				if orientation == "vertical":
					for j in range(shipSize-1):
						currRow+=1
						pieceLocation.append([currRow,currCol])
				else: 
					for j in range(shipSize-1):
						currCol+=1
						pieceLocation.append([currRow,currCol])
				print(pieceLocation)
				time.sleep(1)
				# check if piece fits
				checkCollisions(pieceLocation)
				# if piece fits (no collisions, on board), add to board
				if player == 1:
					addPieceToBoard(playerOne,pieceLocation)
				else:
					addPieceToBoard(playerTwo,pieceLocation)
				piecePlaced = True

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
	# randomly place pieces for both players at start of game
	placePieces(playerOneBottomBoard,playerTwoBottomBoard)


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
