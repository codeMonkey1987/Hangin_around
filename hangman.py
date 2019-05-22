import sys
import os
import random


#open txt document, read every word, and add to list
with open("words.txt") as f:
	wordbank = f.read().splitlines()
	for word in wordbank:
		if len(word) < 3: #remove all words under 3 letters
			wordbank.remove(word)

#create class for all values related to gameplay
class Comp:
	def __init__(self):
		self.wordbank = wordbank
		self.word = ''
		self.word_split = []
		self.blank_spaces = []
		self.revealed = 0

	#function for resetting values on replay
	def reset(self):
		self.word = ''
		self.word_split = []
		self.blank_spaces = []
		self.revealed = 0
		player.wincon = False
		player.attempts = 6
		player.guessed = []

#create class for the user
class Player:
	def __init__(self):
		self.name = ''
		self.attempts = 6
		self.wincon = False
		self.guessed = []

player = Player()
comp = Comp()

#create new game, randomly select a word from our list,
def new_game():
	os.system('clear')
	comp.word = random.choice(comp.wordbank)
	comp.word_split = list(comp.word)
	#create new list of underscores to represent the num of letters in the word
	for i in range(len(comp.word)):
		comp.blank_spaces.append("_")
	#determine if this is first playthrough and establish player name if so
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

#function for printing graphic to screen
def draw_hangman():
	if player.wincon == True:
		print("            __________")
		print("                     ||")
		print("             	     ||")
		print("           {^^}	     ||")
		print("           \\|/	     ||")
		print("            |	     ||")
		print("      _____/_\\______ ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")
		print("     |  |       |  | ||")

	elif player.attempts > 0:
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


#function for testing each guessed letter
def tester(letter):
	counter = len(comp.word)
	for i in range(len(comp.word_split)):
		if letter in comp.word_split[i]:
			#replace underscores with guess in list if correct
			comp.blank_spaces[i] = letter.upper()
			comp.revealed += 1
			#trigger win if all letters are revealed
			if comp.revealed == len(comp.word):
				player.wincon = True

		else:
			counter -= 1

	if counter == 0:
		if player.attempts > 1:
			player.attempts -= 1
			prompt()
		else:
			player.attempts -= 1
			game_over()

#function for prompting user to input guess
def prompt():
	os.system('clear')
	draw_hangman()
	print('\n\n')
	#print either underscore or revealed letter to screen
	print(' '.join(comp.blank_spaces))
	guess = input("\n\n\n\n\nWhat is your guess, {}?: ".format(player.name))
	if len(guess) > 1:
		prompt()
	elif len(guess) == 1:
		if guess.isalpha():
			if guess in player.guessed:
				prompt()
			else:
				player.guessed.append(guess)
				tester(guess.lower())
		else:
			prompt()

#function for end game
def winner():
	os.system('clear')
	draw_hangman()
	print('\n\n')
	print(' '.join(comp.blank_spaces))
	resp = input("\n\n\n\n\nCongratulations, {}! You've guessed the word!\n"
		"Would you like to play again?: (y/n)".format(player.name))
	if len(resp) > 1:
		winner()
	elif resp == 'y':
		comp.reset()
		new_game()
	elif resp == 'n':
		os.system('clear')
		sys.exit()

#function for loss
def game_over():
	os.system('clear')
	draw_hangman()
	print("\n\nThe word was {}". format(comp.word.upper()))
	resp = input('\n\n\nYou have lost.\nNew Game? (y/n): ')
	if len(resp) > 1:
		game_over()
	elif resp == 'y':
		comp.reset()
		new_game()
	elif resp == 'n':
		os.system('clear')
		sys.exit()


#loop handling game progression
def MainGameLoop():
	new_game()
	while player.attempts > 0:
		while player.wincon == False:
			prompt()
		else:
			winner()
	else:
		game_over()

MainGameLoop()