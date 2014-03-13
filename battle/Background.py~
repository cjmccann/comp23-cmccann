import pygame, os, sys
from pygame.locals import *

class Background(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.scrolling = True

		try:
			self.image = pygame.image.load('assets/ram_aras.png').convert_alpha()
			self.rect  = self.image.get_rect()

			self.image_w, self.image_h = self.image.get_size()

			self.screen_w = self.screen.get_size()[0]
			self.screen_h = self.screen.get_size()[1]

			self.x = 0
			self.y = -1 * self.image_h + self.screen_h # starts at the bottom of img

			self.dy = 2

		except pygame.error, message:
			print "Cannot load background image"
			raise SystemExit, message
	
	def update(self):
		#if ((self.y > self.image_h - self.screen_h) and self.scrolling == True:
		#	self.scrolling = False
		#	else:
		self.y += self.dy

	def draw(self):
		if self.scrolling == True:
			draw_pos = self.image.get_rect().move(self.x, self.y)
			self.screen.blit(self.image, draw_pos)
