import pygame

class Battlecruiser(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.screen = screen

		self.image = self.load_image(img_filename)
		self.rect = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()

		self.x = init_x
		self.y = init_y

		self.dx = init_x_speed
		self.dy = init_y_speed

	def update(self):

	def draw(self):
		draw_pos = self.image.get_rect().move(self.x - self

	def load_image(self, image_name):
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()


pygame.init()
screen = pygame.display.set_mode([320, 240])
ship = Battlecruiser()
screen.blit(ship.image, ship.rect)
pygame.display.update()


