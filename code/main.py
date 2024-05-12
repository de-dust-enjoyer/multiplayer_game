from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.RESIZABLE)
		pg.display.set_caption("multiplayer fighting game")
		self.screen = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA)

		self.tmx_maps = {0: load_pygame(join("..", "data", "levels", "test_level.tmx"))}

		self.current_stage = Level()


	def run(self):
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()

			self.current_stage.run()
			self.display.blit(self.resize_screen(), (0,0))
			pg.display.update()


	def resize_screen(self):
		screen = self.screen
		scaled_screen = pg.transform.scale(screen, pg.display.get_surface().get_size())
		return scaled_screen


if __name__ == "__main__":
	game = Game()
	game.run()