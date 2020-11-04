import random

Hangman_Pics = ['''
  +---+
      |
      |
      |
    =====''', '''
  +---+
  O   |
      |
      |
    =====''', '''
  +---+
  O   |
  |   |
      |
    =====''', '''
   +---+
   O   |
  /|   |
       |
     =====''', '''
   +---+
   O   |
  /|\  |
       |
     =====''', '''
   +---+
   O   |
  /|\  |
  /    |
     =====''', '''
   +---+
   O   |
  /|\  |
  / \  |
     =====''']
	  
def getRandomWord(): #returns a random word
	words = 'ant dog frog fox lion'.split()
	randomWord = random.choice(words)
	print('word: ', randomWord)
	return randomWord

def letter_guessed(): #Checks to see if user input enter a letter
	print('gessedLetter: Guess a Letter.')
	guess = input()
	letter = guess.lower()
	
	if letter.isalpha() and len(letter) == 1:
		return letter
	elif len(letter) != 1:
		print('please only type in one letter.')
	else:
		print('please type a letter.')


def display_hangman(hangman): #Will print out the current Hangman Diagram
	#Created a list of the HANGMAN_PIC variable
	hangmanList = list(Hangman_Pics)
	
	for i in range(len(hangmanList)):
		if hangman == i:
			print(hangmanList[i])

def play_again():
	print('Would you like to play again? (yes/no)')
	answer = input()
	
	if answer == ('no'):
		return False
	else:
		return True
		
def missing_letter(word, letter, missing): #Prints missing slots
	print('Missing Letters: ')
	if letter == ' ':
			for i in range(0, len(word)):
				missing.append('_')	
	else:
		for i in range(len(word)):
			if letter == word[i]:
				missing.pop(i)
				missing.insert(i,letter)
	
	if missing != word:
		print('missing():', missing)
		
	return missing
	
def the_game(hangman, word, letter, missing):
	won = True
	guessed = []
	display_hangman(hangman)
	missing_letter(word, letter, missing)
	
	while won == True and hangman != 7:
		l = letter_guessed()
		updatedWord = missing_letter(word, l, missing)
		
		if updatedWord != word:
			if l in word:
				display_hangman(hangman)
			else:
				guessed.insert(hangman,l)
				hangman = hangman + 1
				print(f'You guessed {guessed}')	
				display_hangman(hangman)
		elif hangman == 6:
			print('You ran out of limbs.')
			over = False
		else:
			won = False
			print(f'You guessed {missing}')
			print('You Won!')
		missing = missing	
		
	return play_again()

def start():	
	again = True
	while again == True:
		hangman = 0
		word = list(getRandomWord())
		letter = ' '
		missing = []
		again = the_game(hangman, word, letter, missing)
		
		

start()
