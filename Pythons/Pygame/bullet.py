import pygame
WHITE = (255,255,255)
BLACK = (0,0,0)
class Bullet(pygame.sprite.Sprite):
	def __init__(self,color,width,height,vel):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface([width,height])
		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.vel = vel
		self.rect = self.image.get_rect()
		
	def update(self):
		self.rect.y -= self.vel
		
