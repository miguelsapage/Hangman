from graphics import *

class Hang:
	def __init__(self, win):
		Line(Point(25, 100), Point(25, 200)).draw(win) #Main pole
		Line(Point(25, 100), Point(75, 100)).draw(win)
		Line(Point(75, 100), Point(75, 110)).draw(win) #Rope
		Line(Point(10, 200), Point(40, 200)).draw(win) #Base

		self.errors = 0

	def check_letter(self, letter, word):
		if letter in word:
			return True
		else:
			return False

	def hangman_parts(self):
		man = []
		head = Circle(Point(75, 120), 10)
		man.append(head)
		body = Line(Point(75, 130), Point(75, 170))
		man.append(body)
		right_arm = Line(Point(75,135), Point(85, 145))
		man.append(right_arm)
		left_arm = Line(Point(75,135), Point(65, 145))
		man.append(left_arm)
		right_leg = Line(Point(75,170), Point(85, 185))
		man.append(right_leg)
		left_leg = Line(Point(75,170), Point(65, 185))
		man.append(left_leg)
		return man

	def draw_hangman(self, win, letter, word):
		check = self.check_letter(letter, word)
		man = self.hangman_parts()
		if check == False:
			man[self.errors].draw(win)
			self.errors += 1
		return self.errors

	def end_game(self, errors=0, complete=False):
		if errors == 6:
			return False
		elif complete == True:
			return False
		else:
			return True