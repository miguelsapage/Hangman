"""
This program is a hangman game

Author: Miguel Sapage
"""

from graphics import *
from word import Word

def main():
	choose_word = Word()
	word = choose_word.getWord()
	print(word)

	win = GraphWin('Hangman', 300, 300)


	win.getMouse()
	win.close()

main()