import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):

	def __init__(self, screen, x, y):
		self.x = x
		self.y = y
		self.vx = 2*(random.random()-0.5)
		self.vy = 2*(random.random()-0.5)
		self.theta = 0
		self.dt = 1
		self.screen = screen
		self.image = pygame.image.load("media/planet"+str(random.randint(1,3))+".png")
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.imageW, self.imageH = self.image.get_size()
		pygame.sprite.Sprite.__init__(self)
		
	def checkWalls(self):
		if self.x > 800:
			self.x = 800
			self.vx = 0
		if self.x < 0:
			self.x = 0
			self.vx = 0
		if self.y > 600:
			self.y = 600
			self.vy = 0
		if self.y < 0:
			self.y = 0
			self.vy = 0
	
	def update_velocity(self, px, py):
		vel = 5

		r = [0, 0]
		rUnit = [0, 0]
		force = [0,0]
		r[0] = px - self.x
		r[1] = py - self.y
		rmagSqr = r[0]**2 + r[1]**2
		print rmagSqr
		rmag = math.sqrt(float(rmagSqr))
		rUnit[0] = r[0] / (rmag+1)
		rUnit[1] = r[1] / (rmag+1)

		force[0] = 5e4*rUnit[0] / (rmagSqr+2000)
		force[1] = 5e4*rUnit[1] / (rmagSqr+2000)

		a = force
		self.vx += a[0]*0.1
		self.vy += a[1]*0.1

		turnSpeed = 0.05


	
	def update_position(self):
		self.x += self.vx*self.dt 
		self.y += self.vy*self.dt
		self.checkWalls()
		self.rect.x = self.x
		self.rect.y = self.y
			
		
	def update(self, px, py):
		self.update_velocity(px, py)
		self.update_position()
		
	def blit(self):
		drawpos = self.image.get_rect().move(self.x , self.y)
		self.screen.blit(self.image, drawpos)
		