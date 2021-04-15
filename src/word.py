from graphics import *

class Word:
	def __init__(self):
		#GUI to choose the word
		self.win = GraphWin('Word', 300, 70)

		Text(Point(150, 20), 'Choose the secret word').draw(self.win)
		self.encrypted_word = Text(Point(150, 50), '').draw(self.win)

	def getWord(self):
		word = []
		while True:
			letter = self.win.getKey()
			if letter == 'Return':
				self.win.close()
				break
			elif (len(letter) == 1 and letter.isalpha() == True) or letter == 'space':
				self.encrypt()
				word.append(letter.lower())
			elif letter == 'BackSpace':
				if len(word) == 0:
					continue
				self.undraw_last()
				del word[-1]
		return word

	def encrypt(self):
		self.encrypted_word.undraw()
		self.encrypted_word = Text(Point(150, 50), self.encrypted_word.getText() + '*').draw(self.win)

	def undraw_last(self):
		self.encrypted_word.undraw()
		self.encrypted_word = Text(Point(150, 50), self.encrypted_word.getText()[:-1]).draw(self.win)