from graphics import Point
from button import Button

class End:
	def __init__(self, win, x, y, width, height, name):
		self.end = Button(win, Point(x, y), width, height, name)
		self.end.activate()
		
	def interact(self, click):
		while True:
			if self.end.clicked(click):
				return True
			else:
				return None

	def delete(self):
		self.end.deactivate()
		self.end.undraw()