# The player drops 3 sonar devices at various places in the ocean to locate sunken treasure chests. 
# The sonar devices in this game tell the player how far away the closest treasure chest is, but not 
# in what direction. the player can figure out the location of the treasure chest by the distance of 
# the number given when the sonar device is dropped.

import random
import sys
import math

def getNewBoard():
	# Creating a new 60x15 board data structure 
	board = []
	for i in range(60): # The main list is a list of 60 lists.
		board.append([])
		for j in range(15): # Each list in the main list has 15 single-character strings.
			if random.randint(0,1) == 0: # Different characters will represents the ocean on the board
				board[i].append('`')
			else:
				board[i].append('~')

	return board

def drawBoard(board):
	# The X-axis placed on the top of the board
	tensPlace = ''
	for i in range(1,6):
		tensPlace += (' ' * 9) + str(i)
		
	print('    ' +tensPlace)
	print('   ' +('0123456789'*6))
	
	# We will use a variable that will add an extraSpace to the single-digits in the column
	for row in range(15):
		if row < 10:
			extraSpace = ' '
		else: 
			extraSpace = ''
		# Creating columns for the board
		boardRow = ''
		for column in range(60):
			boardRow += board[column][row]
		
		print('%s%s %s %s' % (extraSpace, row, boardRow, row))
	
	# X-axis for the bottom of the board
	print('   ' +('0123456789'*6))
	print('    ' +tensPlace)
	print()
	
def getRandomChests(level):
	chests = []
	# Creating a list of x and y coordinate where chests are located
	while len(chests) < level:
		for i in range(level):
			newChest = [random.randint(0,59), random.randint(0,14)]
			if newChest not in chests: # Makes sure chests is not already in here
				chests.append(newChest)
			
	return chests
	
def isOnBoard(x,y):
	return x >= 0 and x < 60 and y >= 0 and y < 15 

def playersMove(previousMoves):
	print('Where would you like to drop the sonar. number(0-60), space, number (0-14). or type \'quit')
	while True:
		move = input()
		if move.lower() == 'quit':
			print('Thanks for Playing')
			sys.exit()
			
		move = move.split()
		if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
			if [int(move[0]), int(move[1])] in previousMoves:
				print('Already used this location')
				continue
			
			return [int(move[0]), int(move[1])]
		
		print('Enter an number from (0-59), space, and number (0-14)')

def makeMove(board, chests, x, y):
	# Locate nearest chest and set it as a distance
	# Update the board
	nearestChest = 100
	for cx, cy in chests:
		distance = math.sqrt((cx - x)*(cx - x) + (cy - y)*(cy -y))
		if distance < nearestChest:
			nearestChest = distance
			
	nearestChest = round(nearestChest)
	if nearestChest == 0:
		chests.remove([x,y])
		return('You have found a chest')
	else:
		if nearestChest >= 10:
			board[x][y] = 'X'
			return('Sonar out of range.')
		else:
			board[x][y] = str(nearestChest)
			return('The Sonar detected a chest at a distance of %s away' % nearestChest)
		
print("S O N A R")

while True:
	theBoard = getNewBoard()
	theChests = getRandomChests(3)
	previousMoves = []
	sonars = 20
	drawBoard(theBoard)
	
	while sonars > 0:
		print('You have %s to search with and %s chest to locate' % (sonars, theChests))
		x,y = playersMove(previousMoves)
		previousMoves.append([x,y])
		moveResult = makeMove(theBoard, theChests, x, y)
		print ('a: ',moveResult)
		if moveResult == False:
			continue
		else:
			if moveResult == 'You have found a chest':
				for px, py in previousMoves:
					makeMove(theBoard, theChests, px, py)
			drawBoard(theBoard)
			print(moveResult)
				
		if len(theChests) == 0:
			print('You have found all the chests!')
			break
			
		sonars -= 1
				
	if sonars == 0:
		print('You have ran out of sonars. Game over.')
		print('The location for the sonars were at: ')
		for i in len(theChests):
			print(theChests, ': theChests')
		
	print('Would you like to play again?')
	if not input().lower().startswith('y'):
		sys.exit()

