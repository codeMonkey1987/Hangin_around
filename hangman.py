import sys
import cmd
import os
import random


wordbank = ["apple", "banana", "cake"]
#word = ''
#word_split = []
#blank_spaces = []
#revealed = 0


class Comp:
	def __init__(self):
		self.wordbank = wordbank
		self.word = ''
		self.word_split = []
		self.blank_spaces = []
		self.revealed = 0

	def reset(self):
		self.word = ''
		self.word_split = []
		self.blank_spaces = []
		self.revealed = 0

class Player:
	def __init__(self):
		self.name = ''
		self.attempts = 5
		self.wincon = False

player = Player()
comp = Comp()

def new_game():
	os.system('clear')
	comp.word = random.choice(comp.wordbank)
	comp.word_split = list(comp.word)
	for i in range(len(comp.word)):
		comp.blank_spaces.append("_")

	if player.name == '':		
		print("\n\nLet's play Hangman!\n\n\n\n")
		name = input('What is your name? ')
		if len(name) == 0:
			print("Please enter your name")
			name = input('What is your name? ')
		else:
			player.name = name.title()
			prompt()
	else:
		prompt()



def draw_hangman():
	if player.wincon == True:
		print("            __________")
		print("                     ||")
		print("             	     ||")
		print("           { }	     ||")
		print("           \\|/	     ||")
		print("            |	     ||")
		print("      _____/_\\______ ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")

	if player.attempts > 0:
		print("            __________")
		print("            |        ||")
		print("            |	     ||")
		print("           { }	     ||")
		print("           /|\\	     ||")
		print("            |	     ||")
		print("      _____/_\\______ ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("\nNumber of attempts left: {}".format(player.attempts))

	else:
		print("            __________")
		print("            |        ||")
		print("            |	     ||")
		print("            |	     ||")
		print("            |	     ||")
		print("            |	     ||")
		print("      ____ {xx} ____ ||")
		print("     |  | \\/|\\ /|  | ||")
		print("     |  |   |   |  | ||")
		print("     |  |  / \\  |  | ||")
		print("     |  |       |  | ||")
		print("\nNumber of attempts left: {}".format(player.attempts))


def winner():
	os.system('clear')
	draw_hangman()


def tester(letter):
	counter = len(comp.word)
	for i in range(len(comp.word_split)):
		if letter in comp.word_split[i]:
			comp.blank_spaces[i] = letter.upper()
			comp.revealed += 1
			if comp.revealed == len(comp.word):
				player.wincon = True
				winner()
		else:
			counter -= 1

	if counter == 0:
		if player.attempts > 1:
			player.attempts -= 1
			prompt()
		else:
			player.attempts -= 1
			game_over()



def prompt():
	os.system('clear')
	draw_hangman()
	print('\n\n')
	print(' '.join(comp.blank_spaces))
	guess = input("\n\n\n\n\nWhat is your guess, {}?: ".format(player.name))
	if len(guess) > 1:
		prompt()
	elif len(guess) == 1:
		if guess.isalpha():
			tester(guess.lower())
		else:
			prompt()

#def restart():
#	player.wincon = False
#	word = ''
#	word_split = []
#	blank_spaces.clear()
#	#for i in range(len(word)):
	#	blank_spaces.append("_")
#	player.attempts = 5
#	new_game()


def game_over():
	os.system('clear')
	draw_hangman()
	resp = input('\n\n\nYou have lost.\nNew Game? (y/n): ')
	if resp == 'y':
		comp.reset()
		new_game()
	elif resp == 'n':
		os.system('clear')
		sys.exit()


def MainGameLoop():
	while player.attempts > 0:
		while player.wincon == False:
			prompt()
		else:
			winner()
	else:

		game_over()

	new_game()

MainGameLoop()