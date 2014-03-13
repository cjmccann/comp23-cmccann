import pygame, os, sys, Laser
from pygame.locals import *
from random import randint

class Enemy(pygame.sprite.Sprite):
	IMG_NAME = "assets/mutalisk.gif"

	def load_image(self):
		try:
			image = pygame.image.load(self.IMG_NAME)
		except pygame.error, message:
			print "Cannot load image: " + self.IMG_NAME
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, init_x, init_y, init_dx, init_dy, thePlayer):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen

		self.image = self.load_image()
		self.rect  = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()

		self.x  = init_x
		self.y  = init_y
		self.dx = init_dx
		self.dy = init_dy

		self.active = True

		self.thePlayer = thePlayer

	def update(self):
		if ((self.x + self.dx) <= 0 or (self.x + self.dx) >= self.screen.get_size()[0]):
			self.dx = self.dx * -1
		if ((self.y + self.dy) <= 0 or (self.y + self.dy) >= self.screen.get_size()[1]):
			self.dy = self.dy * -1
		self.x += self.dx
		self.y += self.dy

		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)


	def draw(self):
		draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
		self.screen.blit(self.image, draw_pos)

	def destroy(self):
		try:
			image = pygame.image.load("assets/laser_explosion.gif")
		except pygame.error, message:
			print "Cannot load image: " + "laser_explosion.gif"
			raise SystemExit, message
		self.image = image.convert_alpha()
		self.draw()


if __name__ == "__main__":
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 3
	NUM_SPRITES = 10
	BACKGROUND_COLOR = (255, 255, 255)
	
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('ENEMY WHOAMG')
	
	enemies = []
	for x in xrange(NUM_SPRITES):
		enemies.append(Enemy(screen, randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT),
							 randint(-1 * MAX_SPEED, MAX_SPEED), 
							 randint(-1 * MAX_SPEED, MAX_SPEED), None))
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

		screen.fill(BACKGROUND_COLOR)

		for e in enemies:
			e.update()
			e.draw()

		pygame.display.flip()

