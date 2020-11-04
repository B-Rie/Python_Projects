# This Program is a Guess the Number Game.
# The computer will select a number between 1 - 10 and ask the user to guess.
# After each guess, the computer will tell the user whether the number is too high or to low.
# The user will get 4 attempts.

import random
# This will choose a random number between 1 - 10.
number = random.randint(1, 10)

print('Hello!, please enter your first name.')
name = input()
print(f'Hello {name}, would you like to play a game.')
game = input()

if game.lower() == 'no':
	print('okay, goodbye.')
	
else:
	while True:
		try:
			rangeInt = 4 # Setting the number of attempts allowed to guess.
			print(f'Nice, okay {name}. choose a numer between 1 and 10.')
			for guessTaken in range(rangeInt):
				guess = int(input())
				if guess > number:
					print('you have', rangeInt - (guessTaken+1), ' guesses left')
					print('To HIGH!')
				elif guess < number:
					print('you have', rangeInt - (guessTaken+1), ' guesses left')
					print('To LOW!')
				else:
					print(f'Congrats {name}, you got it!')
					break
		except ValueError:
			print(f"whoops {name}, that wasn't a number.\nTry again.")
			continue
		else:
			break


