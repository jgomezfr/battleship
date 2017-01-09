#!/usr/bin/env python3
import os
import sys
from subprocess import Popen, PIPE

# Waits for a single character of input and returns the string "left", "down", "right", "up", or None.
def getinput():
  original_terminal_state = None

  try:
    original_terminal_state = Popen("stty -g", stdout=PIPE, shell=True).communicate()[0][1:-1]
    # Put the terminal in raw mode so we can capture one keypress at a time instead of waiting for enter.
    os.system("stty raw -echo")
    input = sys.stdin.read(1)

    # The arrow keys are read from stdin as an escaped sequence of 3 bytes.
    escape_sequence = "\x1b"
    ctrl_c = "\003"
    if input == escape_sequence:
      # The next two bytes will indicate which arrow key was pressed.
      character = sys.stdin.read(2)
      arrow_character_codes = dict(D="left", B="down", C="right", A="up")
      return arrow_character_codes.get(character[1], None)
    elif input == ctrl_c:
      sys.exit()
  finally:
    os.system("stty " + str(original_terminal_state))

  return None