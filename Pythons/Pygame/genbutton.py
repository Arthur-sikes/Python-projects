import pygame
DGREY = (100,100,100)
GREY = (200,200,200)
WHITE = (255,255,255)

class GenButton(object):
    def __init__(self,screen,txt,x,y,font,width=120,height=60,ic=DGREY,ac=GREY,action=None):
        self.rect = pygame.Rect([x,y,width,height])
        self.clicked = None
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x+width > mouse[0]> self.rect.x and self.rect.y + height > mouse[1]>self.rect.y and click[0] == 1:
            pygame.draw.rect(screen,ac,self.rect)
            if click[0] == 1 and action != None:
                action()
            if click[0] == 1:
            	self.clicked = True    
            
            
        else:
            self.clicked = False        
            pygame.draw.rect(screen,ic,self.rect)
        msg = font.render(txt,True,WHITE)
        txt_dim = ((self.rect.x+(width/2.856)),(self.rect.y+(height/6.967)))
        screen.blit(msg,txt_dim)
    def status(self):
    	return self.clicked