import pygame
import random


GRAVITY = 0.5
FRICTION =0.99
BLACK = (0,0,0)
class Ball(pygame.sprite.Sprite):
    def __init__(self,color,radius=4):
        super().__init__()    
        self.image = pygame.Surface((radius*2,radius*2))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image,color,[radius,radius],radius)
        self.x_vels = [-6,-3,5,4,6,7,8,9]
        self.y_vels = [-15,-18,-12,-14,-10,10,14,13,18,11]
        self.velocity = [random.choice(self.x_vels),random.choice(self.y_vels)]
        self.rect = self.image.get_rect()
        
        
        
    def update(self):
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        #self.velocity[1] += 0.086
        #self.velocity[1] += GRAVITY
                
    def bounce(self,direction):
       if direction == "top" or direction == "bottom":
           self.velocity[1] *= -1
       elif direction == "left" or direction == "right":
           self.velocity[0] *= -1
         
        
    def reset(self,x,y):
        self.rect.center =(x,y)
        self.velocity =[random.choice(self.x_vels),random.choice(self.y_vels)]




        