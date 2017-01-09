#!/usr/bin/env python3

def clearScreen():
	print("\033[1;1H\033[2J\033[3J")

def drawScreen(graphicsData):
	clearScreen()
	print(" ▁▁▁▁▁▁▁▁▁▁ ")
	print("▕          ▏")
	print("▕  ●●●     ▏")
	print("▕          ▏")
	print("▕    ●     ▏")
	print("▕    ●     ▏")
	print("▕      ●   ▏")
	print("▕          ▏")
	print("▕    ● ●   ▏")
	print("▕          ▏")
	print("▕          ▏")
	print(" ▔▔▔▔▔▔▔▔▔▔ ")
