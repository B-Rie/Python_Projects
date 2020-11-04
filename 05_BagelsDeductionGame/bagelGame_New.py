#Updated

import random

MAX_DIGIT = 3
MAX_GUESSES = 10

def compCode():
	# We don't want repeated numbers. So will have to make a list of numbers 0-9.
	numbers = list(range(10))
	random.shuffle(numbers)
	code = ''
	for i in range(MAX_DIGIT):
		code = code + str(numbers[i])
	return code
	
def playersGuess(num, MAX_DIGIT):
	if num == '':
		print('please enter a 3-Digit number!')
		return False
	
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			print('please enter a 3-digit number!!')
			return False

	if len(num) != MAX_DIGIT:
		print('please enter a 3-Digit number!!!')
		return False
	
	return True
				
def clue(cC, pC):
	if cC == pC:
		return ('You Won!')
	
	clue=[]
	for i in range(len(pC)):
		if pC[i] == cC[i]:
			clue.append('Fermi')
		elif pC[i] in cC:
			clue.append('Pico')
		
	if len(clue) == 0:
		return 'Bagel'
		
	clue.sort()
	return ' '.join(clue)

def playAgain():
	print('Would you like to play again?(yes or no)')
	answer = input()
	if answer == ('no'):
		return False
	else:	
		print('True')
		return True

def display():
	print('''\nI am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say:		That means:
	Bagels       	None of the digits is correct.
	Pico			One digit is correct but in the wrong position.
	Fermi			One digit is correct and in the right position.
I have thought up a number. You have %s guesses to get it.''' % (MAX_GUESSES))

def game():
	cC = compCode()
	attempts = 1
	display()
	while attempts <= 10:
		while True:
			print('Guess #%s' % attempts)
			pC = input()
			guessed = playersGuess(pC, MAX_DIGIT)
			if guessed != False:
				break
				
		print(clue(cC, pC))
		attempts += 1
		
		if cC == pC:
			break
		if attempts > MAX_GUESSES:
			print ('You ran out of guesses, the secret number was %s' % cC)
			break

def start():
	play_again = True
	while play_again:
		game()
		play_again = playAgain()
	
start()
