import pygame
import sys
from ball import Ball
import ball2
from bricks import Brick
from paddle import Paddle

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 1800
HEIGHT = 1000
BACKGROUND_COLOR = (4,26,58)
WHITE = (255,255,255)
ORANGE = (254.36,129.59,0)
LRED = (193.33,29,15)
BROWN = (155,60,0)
YELLOW = (200,170,16)
RED = (255,0,0)
DRED = (175,45,20)
GREEN = (0,255,0)
DGREEN = (30,210,59)
GREY = (210,210,210)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
scores = 0
lives = 3
small_text = pygame.font.SysFont("Comicsansms",45)
large_text = pygame.font.SysFont("Comicsansms",80)
all_sprite_list = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()
paddle = Paddle(width=310,height=10)
paddle.rect.center = (340,800)
all_paddle = pygame.sprite.Group() 
all_paddle.add(paddle)
ball = Ball( GREY,10)
ball.rect.center = (360,500)
all_sprite_list.add(paddle)
all_sprite_list.add(ball)
brick_list =[]
clicked = False
def btn(txt,x,y,width,height,ic,ac,type=""):
    global left_clicked
    global right_clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0]> x and y + height > mouse[1]>y and click[0] == 1:
        pygame.draw.rect(screen,ac,(x,y,width,height))
        if click[0] == 1 and type == 'left':
            paddle.move_left(9)
        elif click[0] == 1 and type =='right':
            paddle.move_right(9)
            
            
    else:
        clicked = False        
        pygame.draw.rect(screen,ic,(x,y,width,height))
    msg = large_text.render(txt,True,WHITE)
    txt_dim = ((x+(width/2.856)),(y+(height/6.967)))
    screen.blit(msg,txt_dim)
    
def draw_environment():
    # Fill the screen with blue-black
        screen.fill(BACKGROUND_COLOR)
        score = small_text.render('score : '+str(scores),True,WHITE)
        life = small_text.render('lives : '+str(lives),True,WHITE)
        screen.blit(score,(0,40))
        screen.blit(life,(0,75))
        pygame.draw.line(screen,ORANGE,(0,120),(1800,120),8)
        left_btn = btn("<",75,1070,120,65,DRED,RED,'left')
        right_btn = btn(">",545,1070,120,65,DGREEN,GREEN,'right')
        for i in range(8):
            bricks = Brick(LRED,95,50)
            bricks_x = (50+(100 * i))
            bricks_y = 151
            bricks.rect.center = (bricks_x,bricks_y)
            brick_list.append(bricks)
            #all_bricks.add(bricks)
        for i in range(7):
            bricks = Brick(YELLOW,90,50)
            bricks_x = (77+(95 * i))
            bricks_y = 205
            bricks.rect.center = (bricks_x,bricks_y)
            #brick_list.append(bricks)
            all_bricks.add(bricks)
            
        for i in range(6):
            bricks = Brick(BROWN,95,50)
            bricks_x = (111 +(100 * i))
            bricks_y = 265
            bricks.rect.center = (bricks_x,bricks_y)                   
            all_bricks.add(bricks)
          
        all_sprite_list.update()
        all_sprite_list.draw(screen)
        #all_bricks.draw(screen)
    # Flip the display
        pygame.display.flip()
        
        

        
        


# Game loop
def main():
    global scores,lives,all_bricks
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if ball.rect.x < 1:
            #ball.velocity[0] = -(ball.velocity[0])
            #ball.velocity[0] *= -1
            #ball.velocity[0] = -ball.velocity[0]
            ball.bounce("left")
        if ball.rect.x>690:
            ball.velocity[0] *= -1
        
        if ball.rect.y >1205:
            lives -=1
            ball.reset(360,500)
            
           
        if paddle.rect.x < 1:
            paddle.rect.x = 1
        if paddle.rect.x > 410:
            paddle.rect.x = 410
            
        """brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
  
  
        'for brick in brick_collision_list:
            # Check the collision side
            if ball.rect.bottom <= brick.rect.top:  # Collision from above
                ball.bounce("top")
            elif ball.rect.top >= brick.rect.bottom:      # Collision from below
                ball.bounce("bottom")
            elif ball.rect.right <= brick.rect.left:  Collision from the left
                ball.bounce("left")
            elif ball.rect.left >= brick.rect.right:  Collision from the right
                ball.bounce("right")
    
            scores += 1
            brick.kill()''
        brick = [brick for brick in all_bricks]
         if pygame.sprite.collide_mask(ball,):
            ball.velocity[1] *= -1
            scores += 1
        for brick in brick_list:
            if pygame.sprite.collide_mask(ball,brick):
                brick_list.remove(brick)
            
            #all_sprite_list.remove(brick)"""
        

            
        for collision in pygame.sprite.spritecollide(ball,all_paddle,False):
            ball.velocity[1] *= -1
           # ball.velocity[0] = ball.velocity[0]
            #ball.bounce()
        draw_environment()
    
    # Cap the frame rate
if __name__=='__main__':
    main()    
    pygame.time.Clock().tick(60)