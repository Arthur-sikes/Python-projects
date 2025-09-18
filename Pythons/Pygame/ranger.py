import pygame
WHITE = (255,255,255)
BLACK = (0,0,0)
class Ranger(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface([width,height])
		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.rect = self.image.get_rect()
	def move_left(self,pix):
		self.rect.x -= pix
	def move_right(self,pix):
		self.rect.x += pix
	def check_bounds(self,left,right):
		if self.rect.x < left:
			self.rect.x = left
		if self.rect.x > right:
			self.rect.x = right
	def move_forward(self,pix):
		self.rect.y += pix
		
	