# Official GAME
import random
import time

def drawBoard(board): 
	# This function prints out the board.
	# 'board' is a list of 10 strings representing 
	# a board using the right keypad. We will ignore index 0.
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])
	
def whoGoesFirst():
	# Randomly choose which player goes first.
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
	
def firstToGo(first):
	# Lets Player type which letter they want to be.
	# The first element will either be a Player or Computer will choose which character to be
	if first == 'player':
		chosen = True
		while chosen:
			print('Do you want to be X or O?')
			letter = input().upper()
			if letter == 'X':
				xo = ['X', 'O']
				chosen = False
			elif letter == 'O':
				xo = ['O', 'X']
				chosen = False
			else:
				print('\nPlease choose either X or O')
				chosen = True
		print('Welcome Player, you chose: ', xo[1])
	else:
		i = random.randint(0,1)
		if i == 0:
			xo = ['X', 'O']
		else:
			xo = ['O', 'X']
		
		print('Computer chose: ', xo[1])
			
	return xo
	
def isWinner(brd, lttr):
	# Given a board and a player's letter, this function returns True if that player has won.
	# We use "brd" instead of "board" and "lttr" instead of "letter" so we don't have to type as much.
	return (brd[1] == lttr and brd[2] == lttr and brd[3] == lttr or # Across the top
	brd[4] == lttr and brd[5] == lttr and brd[6] == lttr or # Across the middle
	brd[7] == lttr and brd[8] == lttr and brd[9] == lttr or # Across the bottom
	brd[1] == lttr and brd[5] == lttr and brd[9] == lttr or # Down the left side
	brd[3] == lttr and brd[5] == lttr and brd[7] == lttr or # Down the middle
	brd[1] == lttr and brd[4] == lttr and brd[7] == lttr or # Down the right side
	brd[2] == lttr and brd[5] == lttr and brd[8] == lttr or # Diagonal
	brd[3] == lttr and brd[6] == lttr and brd[9] == lttr) # Diagonal

def playAgain():
	print('Would you like to play again? (yes/no)')
	answer = input()
	if (answer == 'no' or answer == 'n'):
		return False
	else:
		return True

def boardFull(board):
	if board.count(' ') > 1:
		return False
	else:
		return True

def playersMove(board, pl):
	# INputs player move on the board
	drawBoard(board)
	print('Player, Your move. (1-9)')
	number = int(input())
	if board[number] == ' ':
		board[number] = pl
		return 'computer'
	else:
		print('This box is already taken.\nChose another.')
		return 'player'

def selectRandom(list):
	length = len(list)
	r = random.randrange(0,length)
	return list[r]

def computersMove(board, cl, pl):
	# Will create a list x with open slots that are available
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

	# Will check if computer or player can win
	for let in [cl, pl]:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if isWinner(boardCopy, let):
				return i
	
	# If Corner are Open
	cornersOpen = []
	for i in possibleMoves:
		if i in [1, 3, 7, 9]:
			cornersOpen.append(i)
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move
		
	# If Center is Open
	if 5 in possibleMoves:
		return 5
	
	# If Sides are Open
	edgesOpen = []
	for i in possibleMoves:
		if i in [2, 4, 6, 8]:
			edgesOpen.append(i)
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move
	
def game():
	board = [' '] * 10
	turn = whoGoesFirst()
	pl,cl = firstToGo(turn)
	gameOver = False
	
	while gameOver == False:
		# Players Move
		if turn == 'player': 
			turn = playersMove(board,pl)
			if isWinner(board, pl):
				print("Hooray! You Win!!")
				gameOver = True
			else:
				if boardFull(board):
					print('Board is full. Tied Game!')
					gameOver = True
		# Computers Move
		else:	
			print('Computers Move.')
			move = computersMove(board, cl, pl)
			if board[move] != ' ':
				turn = 'computer'
			else:
				board[move] = cl
				if isWinner(board, cl):
					drawBoard(board)
					print("Computer has Won!")
					gameOver = True
				else:
					if boardFull(board):
						print('Board is full. Tied Game!')
						gameOver = True
					else:
						turn = 'player'

def start():
	again = True
	print("Welcome to Tik Tac Toe")
	while again:
		game()
		again = playAgain()
	

start()	