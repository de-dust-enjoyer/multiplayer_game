import pygame as pg
import sys, socket, random, math, spritesheet, json




class Game:
	def __init__(self):
		pg.init()
		self.screen_size = (1024, 544)
		self.screen = pg.Surface(self.screen_size, pg.SRCALPHA)
		self.fps = 60
		self.display = pg.display.set_mode((self.screen_size[0], self.screen_size[1]), pg.RESIZABLE)
		self.clock = pg.time.Clock()
		self.scaling_factor_x = 1
		self.scaling_factor_y = 1



		# key_pressed_vars:
		self.w_pressed = False
		self.a_pressed = False
		self.s_pressed = False
		self.d_pressed = False
		self.space_pressed = False
		self.mouse_left_pressed = False
		self.mouse_right_pressed = False

	def main_game_loop(self):
		while True:
			self.get_input()
			self.calc_game_state()
			self.render_new_frame()

			# debugging:

			print(f"w_pressed: {self.w_pressed}")
			print(f"a_pressed: {self.a_pressed}")
			print(f"s_pressed: {self.s_pressed}")
			print(f"d_pressed: {self.d_pressed}")
			print(f"space_pressed: {self.space_pressed}")
			print(f"mouse_left_pressed: {self.mouse_left_pressed}")
			print(f"mouse_right_pressed: {self.mouse_right_pressed}")
			
			# update display
			self.display.blit(self.resize_screen(), (0,0))
			pg.display.flip()
			self.clock.tick(self.fps)




	def get_input(self):
		self.mouse_pos = (pg.mouse.get_pos()[0] / self.scaling_factor_x, pg.mouse.get_pos()[1] / self.scaling_factor_y)

		if pg.mouse.get_pressed()[0]:
			self.mouse_left_pressed = True
		if pg.mouse.get_pressed()[2]:
			self.mouse_right_pressed = True

		if not pg.mouse.get_pressed()[0]:
			self.mouse_left_pressed = False
		if not pg.mouse.get_pressed()[2]:
			self.mouse_right_pressed = False

		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit_game()

			if event.type == pg.VIDEORESIZE:
				self.display = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_w:
					self.w_pressed = True
				if event.key == pg.K_a:
					self.a_pressed = True
				if event.key == pg.K_s:
					self.s_pressed = True
				if event.key == pg.K_d:
					self.d_pressed = True
				if event.key == pg.K_SPACE:
					self.space_pressed = True

			if event.type == pg.KEYUP:
				if event.key == pg.K_w:
					self.w_pressed = False
				if event.key == pg.K_a:
					self.a_pressed = False
				if event.key == pg.K_s:
					self.s_pressed = False
				if event.key == pg.K_d:
					self.d_pressed = False
				if event.key == pg.K_SPACE:
					self.space_pressed = False




	def calc_game_state(self):
		pass

	def render_new_frame(self):
		pass
				



	def quit_game(self):
		pg.quit()
		sys.exit()

	def resize_screen(self):
		screen = self.screen
		scaled_screen = pg.transform.scale(screen, pg.display.get_surface().get_size())
		return scaled_screen

game = Game()
game.main_game_loop()