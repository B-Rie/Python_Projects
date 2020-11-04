import random
import sys
WIDTH = 8 # Board is 8 spaces wide
HEIGHT = 8 # Board is 8 spaces tall

def drawBoard(board):
	# Print the board passed to this function. Return None.
	print('  12345678')
	print(' +--------+')
	for y in range(HEIGHT): # Range will start at 0-7
		print('%s|' % (y+1), end ='') # end = '': end a print statement with a string/character and not a newline.
		for x in range(WIDTH):
			print(board[x][y], end='')
		print('|%s' % (y+1))
	print(' +---------+')
	print('  12345678')

def getNewBoard():
	# Create a brand-new data structure board
	board = []
	for i in range(WIDTH):
		board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
	return board

def isValidMove(board, tile, xstart, ystart):
	# Return False if the player's move on space xstart, ystart is invalid.
	# If it is a valid move, return a list of spaces that would become the player's
	# if they made a move here.
	
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False
	
	if tile == 'X':
		otherTile = 'O'
	else:
		otherTile = 'X'
	
	tilesToFlip = []
	for xdirection, ydirection in [[0,1], [1,1], [1,0], [1,-1], [0,-1],[-1,-1], [-1,0],[-1,1]]:
		x, y = xstart, ystart
		x += xdirection
		y += ydirection
		while isOnBoard(x,y) and board[x][y] == otherTile:
			# Keep moving in this x & y direction
			x += xdirection
			y += ydirection
			if isOnBoard(x,y) and board[x][y] == tile:
				# There are pieces to flip over. Go in the reverse
				# direction until we reach the original space, noting
				# all the tiles along the way
				while True:	
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x, y])
	if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move
		return False
	return tilesToFlip
	
def isOnBoard(x, y):
	# Return True if coordinates inputed are located on the board.
	# Using WIDTH and HEIGHT, remember that they're 8, so we need to start at 0 and subtract 1 from W and H.
	return x >= 0 and x <= WIDTH-1 and y >= 0 and y <= HEIGHT-1
	
def getBoardWithValidMoves(board, tile):
	# Return a new board with 'periods' marking the possible moves the player can make
	boardCopy = getBoardCopy(board)
	
	for x, y in getValidMoves(boardCopy, tile):
		boardCopy[x][y] = '.'
	return boardCopy
	
def getValidMoves(board, tile):
	# Return a list of [x, y]'s of valid moves fro the given player to choose from.
	validMoves = []
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if isValidMove(board, tile, x, y) != False:
				validMoves.append([x, y])
	return validMoves
	
def getScoreOfBoard(board):
	# Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'.
	xscore = 0
	oscore = 0
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if board[x][y] == 'X':
				xscore += 1
			elif board[x][y] == 'O':
				oscore += 1
	return {'X':xscore, 'O':oscore} # returning a dictionary
	
def enterPlayersTile():
	# Let Player decided which tile to be
	# Return a list that represents choices [players tile, computers tile]
	tile = ''
	while not (tile == 'X' or tile == 'O'):
		print('Player, please choose which tile to be, \'X\' or \'O\'.')
		tile = input().upper()
	
	# The first element will present the players choice.
	if tile == 'X':
		return ['X','O']
	else:
		return ['O','X']
		
def whoGoesFirst():
	# Randomly choose who goes first.
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def makeMove(board, tile, xstart, ystart):
	# Place a tile at either xstart, ystart, and flip any of the opponents pieces.
	# Return False if this is an invalid move: True if it is.
	tilesToFlip = isValidMove(board, tile, xstart, ystart)
	
	if tilesToFlip == False:
		return False
	
	board[xstart][ystart] = tile
	for x, y in tilesToFlip:
		board[x][y] = tile
	return True
	
def getBoardCopy(board):
	# Get duplicate of the board and return it
	boardCopy = getNewBoard()
	
	for x in range(WIDTH):
		for y in range(HEIGHT):
			boardCopy[x][y] = board[x][y]
	return boardCopy
	
def isOnCorner(x, y):
	# Return True if position is on one of four corners
	return (x == 0 or x == WIDTH-1) and (y == 0 or y == HEIGHT-1) 
	
def getPlayerMove(board, playerTile):
	# let Player enter their move
	# Return the move [x, y] (or return string \'hint\' or \'quit\').'
	DIGITS1to8 = '1 2 3 4 5 6 7 8'.split()
	while True:
		print('Enter your more or type \'hint\' or \'quit\'.')
		move = input().lower()
		if move == 'quit' or move == 'hint':
			return move
		
		if len(move) == 2 and move[0] in DIGITS1to8 and move[1] in DIGITS1to8: 
			x = int(move[0]) - 1
			y = int(move[1]) - 1
			if isValidMove(board, playerTile, x, y) == False:
				continue
			else:
				break
		else:
			print('That\'s not a valid move. Enter the column (1-8) and then the row (1-8).')
			print('For example, 81 will move on the top-right corner.')
			
	return [x,y]

def getComputerMove(board, computerTile):
	# Given a board and the computer's tile, determine where to
	# move and return that move as an [x,y] list.
	possibleMoves = getValidMoves(board, computerTile)
	random.shuffle(possibleMoves) #  Randomize the order of the moves.
	
	# Always go for the corner if available.
	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]
	# Find the highest-scoring move possible.
	bestScore = -1
	for x, y in possibleMoves:
		boardCopy = getBoardCopy(board)
		makeMove(boardCopy, computerTile, x, y)
		score = getScoreOfBoard(boardCopy)[computerTile]
		if score > bestScore:
			bestMove = [x, y]
			bestScore = score
	return bestMove

def printScore(board, playerTile, computerTile):
	scores = getScoreOfBoard(board)
	print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):

		showHints = False
		turn = whoGoesFirst()
		print(turn.upper() + ' will go first')
		
		# Clear the board and place the starting pieces
		board = getNewBoard()
		board[3][3] = 'X'
		board[3][4] = 'O'
		board[4][3] = 'O'
		board[4][4] = 'X'
	
		while True:
			playerValidMoves = getValidMoves(board, playerTile)
			computerValidMoves = getValidMoves(board, computerTile)
			
			if playerValidMoves == [] and computerValidMoves == []:
				return board # No one can move, end the game
				
			if turn == 'player':
				if playerValidMoves != []:
					if showHints:
						validMovesBoard = getBoardWithValidMoves(board, playerTile)
						drawBoard(validMovesBoard)
					else:
						drawBoard(board)
					printScore(board, playerTile,computerTile)
					move = getPlayerMove(board, playerTile)
					if move == 'quit':
						print('Thanks for playing')
						sys.exit()
					elif move == 'hint':
						showHints = not showHints
						continue
					else:
						makeMove(board, playerTile, move[0], move[1])
				turn = 'computer'
				
			elif turn == 'computer': # Computer's turn
				if computerValidMoves != []:
					drawBoard(board)
					printScore(board, playerTile, computerTile)
					move = getComputerMove(board, computerTile)
					makeMove(board, computerTile, move[0], move[1])
				turn = 'player'
				
print('Welcome to Reversegram!')

playerTile, computerTile =enterPlayersTile()

while True:
	finalBoard = playGame(playerTile, computerTile)
	
	# Display the final score
	drawBoard(finalBoard)
	scores = getScoreOfBoard(finalBoard)
	print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
	if scores[playerTile] > scores[computerTile]:
		print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
	elif scores[playerTile] < scores[computerTile]:
		print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
	else:
		print('The game was a tie!')

	print('Do you want to play again? (yes or no)')
	if not input().lower().startswith('y'):
		break