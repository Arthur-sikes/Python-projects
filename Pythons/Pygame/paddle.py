import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color = GREY,width=60,height=40):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.check_bounds()
        
    def check_bounds(self):
        if self.rect.x < 0:
            self.rect.x = 0
            
        if self.rect.x > 700:
            self.rect = 700
        
    def move_left(self,pixels):
        self.rect.x -= pixels
    
    def move_right(self,pixels):
        self.rect.x += pixels
        
        