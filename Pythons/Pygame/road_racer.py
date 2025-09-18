import pygame
import sys
import random 
from car import Car
from button import Button

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 1800
HEIGHT = 1600
BACKGROUND_COLOR = (96, 150, 250)
# Initialize Pygame
pygame.init()

# Set up some constants
BACKGROUND_COLOR = (14,36,68)
WHITE = (200,200,200)
BLACK = (0,0,0)
PURPLE = (117,10,137)
ORANGE = (254.36,129.59,0)
LRED = (193.33,59,45)
BROWN = (155,60,0)
YELLOW = (200,170,16)
RED = (255,0,0)
DRED = (175,45,20)
GREEN = (30,200,30)
DGREEN = (20,145,40)
GREY = (58,58,58)
AQUA = (0,200,200)
BLUE = (39,45,198)
cyan = (0,125,105,0.005)
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

small_text = pygame.font.SysFont("Comicsansms",45)
large_text = pygame.font.SysFont("Comicsansms",80)
scores = 0
color_list = [AQUA,GREEN,YELLOW,BROWN,ORANGE,BLUE,PURPLE]
pos = [90,225,355,495,617]
car_img = ['pyimages/images (1).png','pyimages/car3.png','pyimages/car2.png']
player_car_img = ['pyimages/mySouro2.png']
def count_down_timer(time,x,y,font):
    while time > 0:
        time =time
        t = font.render(str(time),True,WHITE)
        screen.blit(t,(x,y))
        time -= 1
        pygame.time.wait(900)
def draw_environment():
    # Fill the screen with black
    screen.fill(DGREEN)
    pygame.draw.rect(screen,GREY,[35,1,653,1500])
    pygame.draw.line(screen,WHITE,(155,0),(155,1530),6)
    pygame.draw.line(screen,WHITE,(285,0),(285,1530),6)
    pygame.draw.line(screen,WHITE,(425,0),(425,1530),6)
    pygame.draw.line(screen,WHITE,(555,0),(555,1530),6)
    
def text_box(msg,msg2=" ",font=pygame.font.Font(None,35)):
        
        txt_rect = pygame.Rect([150,350,400,150])
        surface = pygame.Surface([txt_rect.width,txt_rect.height], pygame.SRCALPHA)
        pygame.draw.rect(screen,cyan,txt_rect)
        text_surf = font.render(msg,True,BLACK)
        text_surf2 = font.render(msg2,True,BLACK)
        screen.blit(surface,(150,350))
        screen.blit(text_surf,((txt_rect.x+txt_rect.width/3.8646),txt_rect.y+txt_rect.height/2.9657))
        screen.blit(text_surf2,((txt_rect.x+txt_rect.width/3.8646),txt_rect.y+txt_rect.height/1.3987))
#game intro
def game_intro(msg,msg2,font,intro=True):
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_environment()      
        text_box(msg,msg2,font)
        #ticks = pygame.time.Clock().tick(3)
        #txt = large_text.render(str(ticks),True,WHITE)
        #screen.blit(txt,(300,550))
        #count_down_timer(3,300,550,large_text)
        
        pygame.display.flip()
        pygame.time.Clock().tick(15)
        pygame.time.wait(3000)
        intro = False
     
    game_loop()
# Game loop
def game_loop():
    pygame.mixer.music.load('sounds/night-sky.mp3')
    pygame.mixer.music.play(-1)
    scores = 0
    speed = 0.58
    all_sprite_list = pygame.sprite.Group()
    game_over = False
    player_car = Car(random.choice(color_list),110,150)
    player_car.rect.center = (355,900)
    all_sprite_list.add(player_car)
    all_coming_cars = pygame.sprite.Group()
    new_pos = [-400,-493,-560,-999,-209,-600,-365]
    car_speed_list = [8,9.5,11,7.5,6,8.5]
    for i in range(5):
        other_car = Car(random.choice(color_list),130,230)
        other_car.rect.center = (pos[i],-1*(400+(i*900)))
        all_coming_cars.add(other_car)
        all_sprite_list.add(other_car)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for car in all_coming_cars:
            car_speed = random.choice(car_speed_list)
            car.move_forward(car_speed+speed)
            if car.rect.y >1300:
                car.repaint(random.choice(color_list))
                car.rect.y = random.choice(new_pos)
                car_speed = random.choice(car_speed_list)
                speed +=0.05
                scores += 1
        if player_car.rect.x < 40:
            player_car.rect.x = 40
        if player_car.rect.x > 602:
            player_car.rect.x = 602
        draw_environment()   
        all_sprite_list.update()
        all_sprite_list.draw(screen)
        txt =  small_text.render('score : '+str(scores),True,WHITE)
        screen.blit(txt,(10,40))
        left_btn = Button(screen,"<",75,1000,player_car,large_text,4.5,120,65,DRED,RED,'left')
        left_btn.rect.center = (75,1000)
        left_btn.vel = 3
        right_btn = Button(screen,">",545,1000,player_car,large_text,4.5,120,65,DGREEN,GREEN,'right')
        right_btn.rect.center = (545,1070)
        right_btn.vel = 3
        car_collision_list = pygame.sprite.spritecollide(player_car,all_coming_cars,True)
        for car in car_collision_list:
            text_box('GAME OVER!',"your score :"+str(scores),small_text)
            pygame.mixer.music.stop()
            pygame.display.flip()
            pygame.time.wait(3000)
            game_over = True

        # Flip the display
        pygame.display.flip()
        # Cap the frame rate
        pygame.time.Clock().tick(60)
if __name__ == '__main__':
    intro = True
    game_intro('Road Racer Game','By Bullion Cyber',small_text,intro)
    
    #intro = False
    #call the main function
    
    