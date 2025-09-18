import pygame
import sys
from ball import Ball
from brick2 import Brick
from paddle import Paddle
from button import Button

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (17,58,38)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (254.36,129.59,18)
LRED = (193.33,29,15)
BROWN = (165,100,10)
YELLOW = (200,170,0)
RED = (255,0,0)
DRED = (175,45,20)
GREEN = (0,255,0)
DGREEN = (30,210,59)
GREY = (210,210,210)
cyan = (0,125,105,0.005)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
scores = 0
lives = 3
small_text = pygame.font.SysFont("Comicsansms",45)
large_text = pygame.font.SysFont("Comicsansms",80)
all_sprite_list = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()
paddle = Paddle(width=120,height=10,color=GREY)
paddle.rect.center = (350,600)
all_paddle = pygame.sprite.Group() 
all_paddle.add(paddle)
ball = Ball( GREY,10)
ball.rect.center = (360,500)
all_sprite_list.add(paddle)
all_sprite_list.add(ball)
for i in range(8):
    bricks = Brick(RED,95,40)
    bricks_x = (50+(100 * i))
    bricks_y = 151
    bricks.rect.center = (bricks_x,bricks_y)
    all_bricks.add(bricks)
    all_sprite_list.add(bricks)
for i in range(7):
    bricks = Brick(YELLOW,90,40)
    bricks_x = (77+(95 * i))
    bricks_y = 200
    bricks.rect.center = (bricks_x,bricks_y)
    all_bricks.add(bricks)
    all_sprite_list.add(bricks)
for i in range(6):
    bricks = Brick(BROWN,95,40)
    bricks_x = (111 +(100 * i))
    bricks_y = 250
    bricks.rect.center = (bricks_x,bricks_y)                   
    all_bricks.add(bricks)
    all_sprite_list.add(bricks) 
def text_box(msg,font):
        
        txt_rect = pygame.Rect([150,350,400,150])
        surface = pygame.Surface([txt_rect.width,txt_rect.height], pygame.SRCALPHA)
        pygame.draw.rect(screen,cyan,txt_rect)
        text_surf = font.render(msg,True,BLACK)
        screen.blit(surface,(150,350))
        screen.blit(text_surf,((txt_rect.x+txt_rect.width/3.8646),txt_rect.y+txt_rect.height/2.9657))
def draw_environment():
    # Fill the screen with blue-black
        screen.fill(BACKGROUND_COLOR)
        score = small_text.render('score : '+str(scores),True,WHITE)
        life = small_text.render('lives : '+str(lives),True,WHITE)
        screen.blit(score,(0,40))
        screen.blit(life,(0,75))
        pygame.draw.line(screen,ORANGE,(0,120),(1800,120),8)
        left_btn = Button(screen,"<",75,1000,paddle,large_text,10,120,65,DRED,RED,'left')
        left_btn.rect.center = (75,1000)
        right_btn = Button(screen,">",545,1000,paddle,large_text,10,120,65,DGREEN,GREEN,'right')
        right_btn.rect.center = (545,1070)
                
        
        all_sprite_list.draw(screen)
        
    # Flip the display
        
        
def main():
    global lives,scores
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        all_sprite_list.update()
                    
        if ball.rect.x < 1:
               #ball.velocity[0] = -(ball.velocity[0])
               #ball.velocity[0] *= -1
               #ball.velocity[0] = -ball.velocity[0]
            ball.bounce("left")
        if ball.rect.y < 122:
            ball.bounce("top")
        if ball.rect.x>690:
            ball.velocity[0] *= -1
        
        if ball.rect.y >800:
            lives -=1
            ball.reset(360,500)
            if lives == 0:
                text_box('GAME OVER!',small_text)
                pygame.display.flip()
                pygame.time.wait(3000)
                game_over = True
                #pygame.quit()
            
           
        if paddle.rect.x < 1:
            paddle.rect.x = 1
        if paddle.rect.x > 610:
            paddle.rect.x = 610
            
        if pygame.sprite.collide_mask(ball,paddle):
            ball.bounce('bottom')
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,True)
        print(brick_collision_list)
        if brick_collision_list:
            scores += 1
            ball.bounce('top')
            for brick in brick_collision_list:
                print(brick.rect)
                brick.kill()
                all_bricks.remove(brick)
                print('length:',len(all_bricks))
                if len(all_bricks) <= 0:
                    #text = small_text.render("LEVEL COMPLETE", 1, WHITE)
                    #screen.blit(text, (200,300))
                    text_box('LEVEL COMPLETE',small_text)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    game_over = True
        draw_environment()
      
        
        #all_sprite_list.update()
        pygame.display.update()
        pygame.time.Clock().tick(60)
        
if __name__  == '__main__':
        main()
        
        
 



