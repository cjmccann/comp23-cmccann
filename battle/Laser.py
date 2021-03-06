import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
	def load_image (self, image_name):
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
		self.rect  = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()

		self.x = init_x
		self.y = init_y

		self.dx = init_x_speed
		self.dy = init_y_speed

		self.active = True
	
	def update(self):
		self.x = self.x + self.dx
		self.y = self.y + self.dy

		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)


	def draw(self):
		draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
		self.screen.blit(self.image, draw_pos)


if __name__ == "__main__":
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 15
	BACKGROUND_COLOR = (0, 0, 0)
	NUM_SPRITES = 15
	COUNTER_LOCATION = (10, 10)
	LASER_IMAGE = "assets/laser.gif"
	
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('LAZERS')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	counter = 0

	lasers = []
	for i in range(NUM_SPRITES):
		lasers.append(Laser(screen, LASER_IMAGE, randint(1, SCREEN_WIDTH),
							SCREEN_HEIGHT, 0, -1 * randint(1, MAX_SPEED)))

	while True:
		time_passed = clock.tick(FPS)
		text = font.render("Time: " + str(counter) + " (at " + str(FPS) + " FPS)", 1, (255, 255, 255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

		screen.fill(BACKGROUND_COLOR)

		for laser in lasers:
			laser.update()
			laser.draw()

		screen.blit(text, COUNTER_LOCATION)

		counter+=1

		pygame.display.flip()
