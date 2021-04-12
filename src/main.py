"""
This program is a hangman game

Author: Miguel Sapage
"""

from graphics import *
from word import Word
from hang import Hang

def main():
	choose_word = Word()
	word = choose_word.getWord()

	win = GraphWin('Hangman', 600, 300)

	hang = Hang(win)
	end = hang.end_game()

	all_letters = []

	while end:
		letter = win.getKey().lower()
		if len(letter) != 1 or letter.isalpha() == False:
			continue
		elif letter in all_letters:
			print('You already tried that letter')
			continue
		all_letters.append(letter)
		errors = hang.draw_hangman(win, letter, word)

		complete = all(i in all_letters for i in word)

		end = hang.end_game(errors, complete)

	win.close()

main()