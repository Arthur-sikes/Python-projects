import pygame
import grad
BLACK = (0,0,0)
WHITE = (255,255,255)


class Car(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        #self.speed = speed
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent   
        self.image = pygame.surface.Surface([width,height])
        pygame.draw.rect(self.image,self.color,[0,0,width,height])
        self.rect = self.image.get_rect()
        #pygame.transform.scale(self.image,(2,4))
        
#        self.image.fill(WHITE) 
        #self.image.blit(i,self.rect)
        #self.image.set_colorkey(WHITE)
        #self.set_transparent()
        
        
        # Fetch the rectangle object that has the dimensions of the image.    
        
    '''def set_transparent(self):
        color = grad.gen(150)
        for col in color:
            self.image.set_colorkey(col)'''
            
    def move_right(self, pix):
        self.rect.x += pix
        
    def move_left(self, pix):
        self.rect.x -= pix
        
    def move_forward(self,pix):
        self.rect.y += pix
        
    def repaint(self,color):
        self.color = color
    def change_speed(self,pix):
        self.speed = pix
        