
import cmd
import os
import random

wincon = False
wordbank = []
word = ''


class Player:
	def __init__(self):
		self.name = ''
		self.strikes = 0

player = Player()

def new_game():
	os.system('clear')
	print("\n\nLet's play Hangman!\n\n\n\n")
	name = input('What is your name?')
	if len(name) == 0:
		print("Please enter your name")
		name = input('What is your name?')
	else:
		player.name = name.title()
		prompt()

def draw_hangman():
	if player.strikes < 5:
		print("       __________")
		print("       |        ||")
		print("       |	||")
		print("      { }	||")
		print("      /|\\	||")
		print("       |	||")
		print(" _____/_\\______	||")
		print("|  |  	   |  |	||")
		print("|  |       |  | ||")
		print("|  |       |  | ||")
		print("|  |       |  | ||")
		print("       	   ============")
	else:
		print("       __________")
		print("       |        ||")
		print("       |	||")
		print("       |	||")
		print("       |	||")
		print("       |	||")
		print(" ____ {xx} ____	||")
		print("|  | \\/|\\ /|  |	||")
		print("|  |   |   |  | ||")
		print("|  |  / \\  |  | ||")
		print("|  |       |  | ||")
		print("       	   ============")


def winner():
	os.system('clear')

def prompt():
	os.system('clear')
	draw_hangman()
	guess = input("What is your guess, {}?: ".format(player.name))


def game_over():
	os.system('clear')
	draw_hangman()


def MainGameLoop():
	while player.strikes < 3:
		while wincon == False:
			prompt()
		else:
			winner()
	else:
		game_over()


new_game()