import pygame, os, sys
from pygame.locals import *

class Battlecruiser(pygame.sprite.Sprite):

	def load_image(self, image_name):
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, img_filename, init_x, init_y, 
						 init_x_speed, init_y_speed):
		pygame.sprite.Sprite.__init__(self)
		
		self.screen = screen

		self.image = self.load_image(img_filename)
		self.rect = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()

		self.x = init_x
		self.y = init_y

		self.dx = init_x_speed
		self.dy = init_y_speed

		self.active = True

		self.lasers = []

	def update(self):
		x = 0

	def draw(self):
		self.screen.blit(self.image, (0, 0))

	def addLaser(self):
		x = 0

	def move(self, keyType):
		if keyType == K_UP:
			self.y-=3
		elif keyType == K_DOWN:
			self.y+=3
		elif keyType == K_LEFT:
			self.x-=3
		elif keyType == K_RIGHT:
			self.x+=3


if __name__ == "__main__":
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 10
	BACKGROUND_COLOR = (0, 0, 0)
	NUM_SPRITES = 10
	
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('BATTLECRUISERZ')
	clock = pygame.time.Clock()

	battlecruiser = Battlecruiser(screen, "assets/battlecruiser.gif", SCREEN_WIDTH/2,
								  SCREEN_HEIGHT/2, 0, 0)

	while True:
		time_passed = clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == K_SPACE):
					battlecruiser.addLaser()
				if (event.key == K_UP || event.key == K_DOWN || 
						event.key == K_LEFT || event.key == K_RIGHT):
					battlecruiser.move(event.key)


		screen.fill(BACKGROUND_COLOR)


		pygame.display.flip()

