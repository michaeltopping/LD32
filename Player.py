import pygame
import random
import math

class Player(pygame.sprite.Sprite):

	def __init__(self, screen, x, y):
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 0
		self.theta = 0
		self.dt = 1
		self.score = 0
		self.screen = screen
		self.rot = 0
		self.imageOrig = pygame.image.load("media/player.png")
		self.imageOrig = self.imageOrig.convert_alpha()
		self.image = self.imageOrig
		self.rect = self.image.get_rect()
		self.imageW, self.imageH = self.image.get_size()
		pygame.sprite.Sprite.__init__(self)
		
	def checkWalls(self):
		if self.x > 800:
			self.x = 800
		if self.x < 0:
			self.x = 0
		if self.y > 600:
			self.y = 600
		if self.y < 0:
			self.y = 0
	
	def update_velocity(self, direction):
		vel = 5
		self.vx = 0
		self.vy = 0
		turnSpeed = 0.05
		if 'L' in direction:
			self.vx += -vel
		if 'R' in direction:
			self.vx += vel
		if 'U' in direction:
			self.vy += -vel
		if 'D' in direction:
			self.vy += vel

	
	def update_position(self):
		self.x += self.vx*self.dt
		self.y += self.vy*self.dt
		self.checkWalls()
		self.rect.centerx = self.x
		self.rect.centery = self.y
			
		
	def update(self, direction):
		self.update_velocity(direction)
		self.update_position()
		oldCenter = self.rect.center
		self.rot += 1
		self.image = pygame.transform.rotate(self.imageOrig, self.rot)
		self.rect.center = oldCenter
		
	def blit(self):
		drawpos = self.image.get_rect().move(self.rect.centerx, self.rect.centery)
		self.screen.blit(self.image, drawpos)
		