# battleship

## Features

### board
	- 10x10 for current player
	- 10x10 for opponent
### ship tokens
	- carrier (5)
	- battleship (4)
	- cruiser (3)
	- submarine (3)
	- destroyer (2)

	 ▁▁▁▁▁▁▁▁▁▁
	▕          ▏
	▕  ●●●     ▏
	▕          ▏
	▕    ●     ▏
	▕    ●     ▏
	▕      ●   ▏
	▕          ▏
	▕    ● ●   ▏
	▕          ▏
	▕          ▏
	 ▔▔▔▔▔▔▔▔▔▔
	 ▁▁▁▁▁▁▁▁▁▁
	▕█████     ▏
	▕       ●  ▏
	▕    █     ▏
	▕    ●     ▏
	▕    █  ██ ▏
	▕    █     ▏
	▕          ▏
	▕      ███ ▏
	▕          ▏
	▕   ███    ▏
	 ▔▔▔▔▔▔▔▔▔▔

### battleship splash screen
	- load controls from file
	- load scores from leaderboard file

### welcome menu
	- start new game
	- load saved game (only if saved games exist)
	- high scores leaderboard (only if leaderboard is not empty)
	- controls
	- quit
### player selection screen
	- one player (vs AI)
	- two player (hotseat)
	- two player (online)
	- no player (AI vs AI)
### AI difficulty selection
	- easy: random missiles
	- medium: random missiles, concentrate fire around hits
	- hard: probability density function 
### player one/two splash screen (hotseat only)
### display board and place pieces
	- initialize piece placement
		- randomized
		- collision detection
	- piece movement (arrow keys)
	- piece rotation (space key)
	- piece selection (tab and color)
	- finalize placement of all pieces (enter key)
	- collision detection 
		- when finalizing placement only
		- with other pieces
		- with edge of board
### AI board and piece placement (one player only)
	- easy: randomly place pieces (same as initialization for player)
	- medium: random but replace if pieces are adjacent
	- hard: same as medium
### gameplay start
	- change to two-board view
		- top board: tracking board for this player's guesses (enemy board)
		- bottom board: tracking board for this player's ships (player board)
	- randomly select start player
		- indicate player turn on screen
	- player one/two splash screen (hotseat only)
	- initialize board with current player's ship placement
	- graphics: 
		- cursor: blue circle
		- hit: red circle
		- miss: white circle
		- cursor over hit or miss: grey circle
	- keys: 
		- move cursor: arrow keys
		- fire: enter key
		- escape: save and quit
			- save game splash screen
			- hotseat only: enter name for current player's turn
			- enter to confirm save and exit to menu
	- check win condition after every turn
	- AI turn: 
		- [see above](#AI difficulty selection)
	- winner splash screen! 
	- score: missiles used (winners only)
	- show leaderboard top 10 scores
		 - local saved top scores
		 - save to leaderboard.csv
		 - save as a binary file to prevent tampering!
		 - save as encrypted file 
	- if new high score, enter player username
	- hit enter: go back to welcome menu
### load saved game menu
	- display list of saved games
	- game type and timestamp
	- for hotseat games: "Two player, Julieta's turn" include player name
	- arrow keys move up/down list
	- enter to select game
		- display board
		- "load this game?"
		- enter to confirm 
		- backspace to cancel, back to saved games list
		- escape to go back to welcome menu
### controls screen
	- display current controls
	- arrow keys to scroll through controls
	- enter to edit
	- press new key for control
	- update display of controls
	- save controls to file
	- reset to defaults option



