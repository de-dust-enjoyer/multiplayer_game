from settings import *

class Level:
	def __init__(self):
		self.display = pg.display.get_surface()
		self.screen = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA)

	def run(self):
		self.screen.fill("grey")
		self.display.blit(self.resize_screen(), (0,0))

	def resize_screen(self):
		screen = self.screen
		scaled_screen = pg.transform.scale(screen, pg.display.get_surface().get_size())
		return scaled_screen
