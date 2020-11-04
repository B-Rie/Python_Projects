#The player decides between two caves, which hold either treasure or certain doom.

import random
import time

def introduction():
	print('''Welcome Player.
	Would you like to play a game? (yes or no)''')
	
	decision = input('> ')
	
	while True:
		try:
			if decision.lower() == 'no' or decision.lower() == 'n':
				print('good-bye')
				break
			else:
				start()
		except ValueError:
			print('Sorry player, didn\'t understand your input.\nPlease type again.')
			continue
		else:
			break

def start():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.
	Which cave will you go into? (1 or 2)''')
	caves()
	
def caves():
	caveNumber = input('> ')
	
	if caveNumber.lower() == '1':
		first_path()
	elif caveNumber.lower() == '2':
		second_path()
	else:
		print("Try that again.")
		caves()

def first_path():
	print('''You approach the cave...
	It is dark and spooky...
	A large dragon jumps out in front of you! He opens his jaws and...''')
	time.sleep(2)
	print('''Gobbles you down in one bite!
	Do you want to play again? (yes or no)''')
	play_again()
	

def second_path():
	print('''You approach the cave...
	It is dark and spooky...
	The cave goes on... 
	You find a Torch on the wall and light it.''')
	time.sleep(2)
	print('''The light brightens the room and so see nothing but gold piled in the cave.
	Do you want to play again? (yes or no)''')
	play_again()

		
def play_again():
	choice = input('> ')
	if choice.lower() == 'yes':
		start()
	elif choice.lower() == 'no':
		print("good-bye")
	else:
		print("sorry, what was that?")
		play_again()
		

introduction()
		