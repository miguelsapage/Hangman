from graphics import *

class Format:
	def __init__(self, word, win):
		self.word = word
		self.win = win

	def split_words(self):
		phrase = ''.join(self.word).split('space')
		return phrase

	def make_lines(self):
		self.phrase = self.split_words()
		if len(self.phrase) > 7:
			lines = 2
		else:
			lines = 1
		return lines

	def position_lines(self):
		self.lines = self.make_lines()
		self.lines_coords = []
		height = self.win.getHeight()
		if self.lines == 1:
			y = height / 2
			self.lines_coords.append(y)
		elif self.lines == 2:
			y = height / 2
			self.lines_coords.append(y - 30)
			self.lines_coords.append(y + 30)

	def position_letters(self, x_coord):
		self.position_lines()
		x = x_coord
		letters_coords = []
		for i in self.phrase:
			if self.lines == 2:
				for j in self.phrase[self.phrase.index(i)]:
					if self.phrase.index(i) < len(self.phrase) / 2:
						Line(Point(x, self.lines_coords[0]), Point(x + 10, self.lines_coords[0])).draw(self.win)
						letters_coords.append(Point(x + 5, self.lines_coords[0] - 10))
						x += 15
					else:
						Line(Point(x, self.lines_coords[1]), Point(x + 10, self.lines_coords[1])).draw(self.win)
						letters_coords.append(Point(x + 5, self.lines_coords[1] - 10))
						x += 15
				if self.phrase.index(i) == len(self.phrase) / 2 - 1 or self.phrase.index(i) == len(self.phrase) / 2 - 0.5:
					x = x_coord
			elif self.lines == 1:
				for j in self.phrase[self.phrase.index(i)]:
					Line(Point(x, self.lines_coords[0]), Point(x + 10, self.lines_coords[0])).draw(self.win)
					letters_coords.append(Point(x + 5, self.lines_coords[0] - 10))
					x += 15
			x += 15
		return letters_coords