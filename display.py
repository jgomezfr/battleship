#!/usr/bin/env python3

COLOR_NORMAL  = "\x1B[0m"
COLOR_RED     = "\x1B[31m"
COLOR_GREEN   = "\x1B[32m"
COLOR_YELLOW  = "\x1B[33m"
COLOR_BLUE    = "\x1B[34m"
COLOR_MAGENTA = "\x1B[35m"
COLOR_CYAN    = "\x1B[36m"
COLOR_WHITE   = "\x1B[37m"

def clearScreen():
	sys.stdout.write("\033[1;1H\033[2J\033[3J")

def changeColor(color):
	sys.stdout.write({
		'normal': COLOR_NORMAL,
		'red':    COLOR_RED,
		'green':  COLOR_GREEN,
		'yellow': COLOR_YELLOW,
		'blue':   COLOR_BLUE,
		'magenta':COLOR_MAGENTA,
		'cyan':   COLOR_CYAN,
		'white':  COLOR_WHITE
	}[color])

def colortest():
	for i in ('normal','red','green','yellow','blue','magenta','cyan','white'):
		changeColor(i)
		print(i)
	changeColor('normal')

def drawBoard(board,cursor):
	print(" ▁▁▁▁▁▁▁▁▁▁▁ ")
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
		rowDisplayString+= "▕"
		print(rowDisplayString)
	print(" ▔▔▔▔▔▔▔▔▔▔▔ ")

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