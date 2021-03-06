import pygame, os, sys, Laser
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

	def update(self, keyType):
		# Moves the unit and adds momentum
		if keyType == K_UP:
			self.y-=3
			self.dy-= 4 
		elif keyType == K_DOWN:
			self.y+=3
			self.dy+= 4 
		elif keyType == K_LEFT:
			self.x-=3
			self.dx-= 4 
		elif keyType == K_RIGHT:
			self.x+=3
			self.dx+= 4
		elif keyType == None:
			self.x += self.dx
			self.y += self.dy
			# Slow momentum of ship
			if self.dx > 0:
				self.dx -= .2
			elif self.dx < 0:
				self.dx += .2
			if self.dy > 0:
				self.dy -= .2
			elif self.dy < 0:
				self.dy += .2
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

	def draw(self):
		draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
		self.screen.blit(self.image, draw_pos)

	def laserClip(self):
		try:
			sound = pygame.mixer.Sound("assets/laser.wav")
			sound.play()
		except pygame.error, message:
			pass

if __name__ == "__main__":
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 10
	BACKGROUND_COLOR = (0, 0, 0)
	NUM_SPRITES = 10
	LASERS = []	
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('BATTLECRUISERZ')
	clock = pygame.time.Clock()

	battlecruiser = Battlecruiser(screen, "assets/battlecruiser.gif", SCREEN_WIDTH/2,
								  SCREEN_HEIGHT/2, 0, 0)

	while True:
		time_passed = clock.tick(FPS)

		screen.fill(BACKGROUND_COLOR)

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == K_SPACE):
					LASERS.append(Laser.Laser(screen, "assets/laser.gif", battlecruiser.x, 
						          battlecruiser.y - (battlecruiser.image_h/2), 0, -7))
					battlecruiser.laserClip()
				if (event.key == K_UP or event.key == K_DOWN or 
						event.key ==  K_LEFT or event.key == K_RIGHT):
					battlecruiser.update(event.key)
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

		battlecruiser.draw()
		
		for l in LASERS:
			l.update()
			l.draw()

		pygame.display.flip()

