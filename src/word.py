from graphics import *

class Word:
	def __init__(self):
		self.win = GraphWin('Word', 200, 70)

		Text(Point(100, 20), 'Choose the secret word').draw(self.win)
		self.encrypted_word = Text(Point(100, 50), '').draw(self.win)

	def getWord(self):
		word = []
		while True:
			letter = self.win.getKey()
			if letter == 'Return':
				self.win.close()
				break
			elif len(letter) == 1:
				self.encrypt()
				word.append(letter.lower())
		return word

	def encrypt(self):
		self.encrypted_word.undraw()
		self.encrypted_word = Text(Point(100, 50), self.encrypted_word.getText() + '*').draw(self.win)