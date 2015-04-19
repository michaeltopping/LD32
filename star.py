import pygame
import random
import math

class Star(pygame.sprite.Sprite):

	def __init__(self, screen, x, y):
		self.x = x
		self.y = y
		self.screen = screen
		self.image = pygame.image.load("media/star.png")
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.imageW, self.imageH = self.image.get_size()
		pygame.sprite.Sprite.__init__(self)
		self.rect.x = x
		self.rect.y = y

		
	def blit(self):
		self.screen.blit(self.image, self.rect)
		