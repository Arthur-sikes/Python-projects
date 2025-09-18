import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)

class Brick(pygame.sprite.Sprite):
    def __init__(self,color,width=60,height=40):
        #sleft_btn = btn("<",75,1070,120,65,DRED,RED,'left')uper().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.color = color
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,self.color,self.rect)
        