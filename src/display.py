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
		if len(self.phrase) > 6:
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
		letters_slots = []
		for i in self.phrase:
			if self.lines == 2:
				for j in self.phrase[self.phrase.index(i)]:
					if self.phrase.index(i) < len(self.phrase) / 2:
						Line(Point(x, self.lines_coords[0]), Point(x + 10, self.lines_coords[0])).draw(self.win)
						letters_slots.append(Point(x + 5, self.lines_coords[0] - 10))
						x += 15
					else:
						Line(Point(x, self.lines_coords[1]), Point(x + 10, self.lines_coords[1])).draw(self.win)
						letters_slots.append(Point(x + 5, self.lines_coords[1] - 10))
						x += 15
				if self.phrase.index(i) == len(self.phrase) / 2 - 1 or self.phrase.index(i) == len(self.phrase) / 2 - 0.5:
					x = x_coord - 15
			elif self.lines == 1:
				for j in self.phrase[self.phrase.index(i)]:
					Line(Point(x, self.lines_coords[0]), Point(x + 10, self.lines_coords[0])).draw(self.win)
					letters_slots.append(Point(x + 5, self.lines_coords[0] - 10))
					x += 15
			x += 15
		return letters_slots

class Letters:
	def __init__(self, win, letters_slots, words_without_spaces):
		self.win = win
		self.letters_slots = letters_slots
		self.words_without_spaces = words_without_spaces

	def positions_to_display(self, letter):
		index_list = []
		if letter in self.words_without_spaces:
			for i in range(len(self.words_without_spaces)):
				if self.words_without_spaces[i] == letter:
					index_list.append(i)
		return index_list

	def display_letter(self, letter):
		index_list = self.positions_to_display(letter)
		for i in index_list:
			Text(self.letters_slots[i], letter.upper()).draw(self.win)

class Lost:
	def __init__(self, win, letters_slots, words_without_spaces):
		self.win = win
		self.letters_slots = letters_slots
		self.words_without_spaces = words_without_spaces

	def display_result(self):
		for i in range(len(self.words_without_spaces)):
			Text(self.letters_slots[i], self.words_without_spaces[i].upper()).draw(self.win)