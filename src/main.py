"""
This program is a hangman game

Author: Miguel Sapage
"""

from graphics import *
from word import Word
from hang import Hang
from display import *
from end import End

def main():
	choose_word = Word()
	word = choose_word.getWord()
	words_without_spaces = list(word)
	for i in word:
		if i == 'space':
			words_without_spaces.remove(i)

	win = GraphWin('Hangman', 600, 300)

	hang = Hang(win)
	slots_display = Format(word, win)
	letters_slots = slots_display.position_letters(150)

	end = hang.end_game()

	letters_class = Letters(win, letters_slots, words_without_spaces)

	all_letters = []

	while end:
		letter = win.getKey().lower()
		if len(letter) != 1 or letter.isalpha() == False:
			continue
		elif letter in all_letters:
			print('You already tried that letter')
			continue
		all_letters.append(letter)
		errors = hang.draw_hangman(letter, words_without_spaces)

		letters_class.display_letter(letter)

		complete = all(i in all_letters for i in words_without_spaces)

		end = hang.end_game(errors, complete)

	if complete == True:
		Text(Point(325, 40), 'You got it! Amazing!').draw(win)
	elif complete == False:
		lost = Lost(win, letters_slots, words_without_spaces)
		lost.display_result()
		Text(Point(325, 40), 'You lost...try again').draw(win)

	quit_button = End(win, 570, 280, 40, 20, 'Quit')
	restart_button = End(win, 515, 280, 60, 20, 'Restart')

	while True:
		click = win.getMouse()
		if quit_button.interact(click):
			break
		elif restart_button.interact(click):
			win.close()
			main()
			break

	win.close()

main()