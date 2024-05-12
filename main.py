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

		self.menu = False
		self.game_end = False



		# key_pressed_vars:
		self.w_pressed = False
		self.a_pressed = False
		self.s_pressed = False
		self.d_pressed = False
		self.space_pressed = False
		self.mouse_left_pressed = False
		self.mouse_right_pressed = False


		# importing stuff

		#	 font
		self.font_10 = pg.font.Font("assets/font/pixel_font.otf", 10)
		self.font_12 = pg.font.Font("assets/font/pixel_font.otf", 12)
		self.font_14 = pg.font.Font("assets/font/pixel_font.otf", 14)
		self.font_16 = pg.font.Font("assets/font/pixel_font.otf", 16)
		self.font_18 = pg.font.Font("assets/font/pixel_font.otf", 18)
		self.font_20 = pg.font.Font("assets/font/pixel_font.otf", 20)
		self.font_25 = pg.font.Font("assets/font/pixel_font.otf", 25)
		self.font_30 = pg.font.Font("assets/font/pixel_font.otf", 30)
		self.font_35 = pg.font.Font("assets/font/pixel_font.otf", 35)
		self.font_40 = pg.font.Font("assets/font/pixel_font.otf", 40)
		self.font_45 = pg.font.Font("assets/font/pixel_font.otf", 45)
		self.font_50 = pg.font.Font("assets/font/pixel_font.otf", 50)
		self.font_60 = pg.font.Font("assets/font/pixel_font.otf", 60)
		self.font_70 = pg.font.Font("assets/font/pixel_font.otf", 70)
		self.font_80 = pg.font.Font("assets/font/pixel_font.otf", 80)
		self.font_90 = pg.font.Font("assets/font/pixel_font.otf", 90)
		self.font_100 = pg.font.Font("assets/font/pixel_font.otf", 100)
		self.font_150 = pg.font.Font("assets/font/pixel_font.otf", 150)
		self.font_200 = pg.font.Font("assets/font/pixel_font.otf", 200)

	def main_game_loop(self):
		while True:
			self.get_input()
			self.calc_game_state()
			self.render_new_frame()

			# debugging:

			
			
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
		if self.menu:
			pass
		elif self.game_end:
			pass
		else:
			pass

	def render_new_frame(self):
		self.screen.fill((28, 5, 42))
		if self.menu:
			pass
		elif self.game_end:
			pass
		else:
			pass


				



	def quit_game(self):
		pg.quit()
		sys.exit()

	def resize_screen(self):
		screen = self.screen
		scaled_screen = pg.transform.scale(screen, pg.display.get_surface().get_size())
		return scaled_screen

	def render_text_center(self, text:str, font:pg.font.Font, color:tuple, pos:tuple):
		text = font.render(text, False, color)
		text_rect = text.get_rect(center= pos)
		self.screen.blit(text, text_rect)

game = Game()
game.main_game_loop()