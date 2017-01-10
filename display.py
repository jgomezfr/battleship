#!/usr/bin/env python3

def clearScreen():
	print("\033[1;1H\033[2J\033[3J")

def drawBoard(board,cursor):
	print(" ▁▁▁▁▁▁▁▁▁▁ ")
	for row in range(len(board)):
		rowDisplayString = "▕"
		for col in range(len(board[0])):
			if cursor != None:
				if row == cursor[0] and col == cursor[1]:
					rowDisplayString+="◎"
					continue
			if board[row][col] == 0:
				rowDisplayString+=" "
			else:
				rowDisplayString+="●"
		rowDisplayString+="▏"
		print(rowDisplayString)
	print(" ▔▔▔▔▔▔▔▔▔▔ ")	

def drawScreen(topBoard,bottomBoard,cursor):
	clearScreen()
	drawBoard(topBoard,cursor)
	drawBoard(bottomBoard,None)

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