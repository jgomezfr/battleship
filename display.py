#!/usr/bin/env python3

def clearScreen():
	print("\033[1;1H\033[2J\033[3J")

def drawBoard(board):
	print(" ▁▁▁▁▁▁▁▁▁▁ ")
	for row in board:
		rowDisplayString = "▕"
		for col in row:
			if col == 0:
				rowDisplayString+=" "
			else:
				rowDisplayString+="●"
		rowDisplayString+="▏"
		print(rowDisplayString)
	print(" ▔▔▔▔▔▔▔▔▔▔ ")	

def drawScreen(topBoard,bottomBoard):
	clearScreen()
	drawBoard(topBoard)
	drawBoard(bottomBoard)

	# print(" ▁▁▁▁▁▁▁▁▁▁ ")
	# print("▕          ▏")
	# print("▕  ●●●●●   ▏")
	# print("▕        ● ▏")
	# print("▕    ●   ● ▏")
	# print("▕    ●     ▏")
	# print("▕    ●     ▏")
	# print("▕          ▏")
	# print("▕    ●●●   ▏")
	# print("▕          ▏")
	# print("▕ ●●●●     ▏")
	# print(" ▔▔▔▔▔▔▔▔▔▔ ")

def playerOneSplash():
	clearScreen()
	print("Ready, Player One?")

def playerTwoSplash():
	clearScreen()
	print("Ready, Player Two?")