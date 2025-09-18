import pygame
import random
from genbutton import GenButton
from ranger import Ranger
from bullet import Bullet
LIGHT_BLUE = (100,225,255)
RED = (255,0,0)
GREEN = (0,220,0)
BROWN = (137,81,42)
YELLOW = (200,170,0)
DGOLD = (170,120,19)
ORANGE = (254.36,129.59,18)
DORANGE = (154,89,20)
LRED = (193.33,29,15)
DRED = (175,45,20)
OGREEN = (0,255,0)
DGREEN = (30,180,49)
GREY = (210,210,210)
cyan = (0,125,105,0.005)
pygame.init()
scores = 0
lives = 3
small_text = pygame.font.SysFont("Comicsansms",45)
large_text = pygame.font.SysFont("Comicsansms",80)
def shoot(bullet_list):
	for bullet in bullet_list:
		for i in range(190):
			bullet.fire(3)
	pass
def draw_environment(screen,player):
	screen.fill(LIGHT_BLUE)
	pygame.draw.rect(screen,BROWN,[0,1060,1000,250])
	pygame.draw.rect(screen,GREEN,[0,1029,1000,30])
	left_btn = GenButton(screen,"<",75,1090,large_text,120,65,DRED,RED, lambda : player.move_left(19))
	left_btn.rect.center = (75,1000)
	right_btn = GenButton(screen,">",545,1090,large_text,120,65,DGREEN,GREEN,lambda: player.move_right(19))
	right_btn.rect.center = (545,1070)
def create_enemy(pos,pos2,all_enemy):
	for i in range(3):
		enemy = Ranger(GREEN,120,180,)
		enemy.rect.center =(random.choice(pos),random.choice(pos2))
		all_enemy.add(enemy)
def main():
	width = 800
	height = 600
	pos = [90,225,355,495,617]
	pos2 = [-600,-400,-1500,-900,-200,-150]
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Space Invaders")
	space_ranger = Ranger(YELLOW,120,180,)
	player_rect = pygame.Rect([300,850,120,180])
	space_ranger.rect.center = player_rect.center
	bull = [ ]
	all_sprite_list = pygame.sprite.Group()
	all_sprite_list.add(space_ranger)
	all_enemy = pygame.sprite.Group()
	all_bullets = pygame.sprite.Group()
	create_enemy(pos,pos2,all_enemy)
	all_sprite_list.add(all_enemy)
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		space_ranger.check_bounds(1,622)
		draw_environment(screen,space_ranger)
		shoot_btn = GenButton(screen,"shoot",300,1090,small_text,190,65,DORANGE,ORANGE)
		for i in range(16):
		    if shoot_btn.status():
			    bullet = Bullet(DGOLD,10,15,30)
			    bullet.rect.center = ((space_ranger.rect.left+60),player_rect.top)
			    all_sprite_list.add(bullet)
			    all_bullets.add(bullet)
			    bull.append(bullet)
			    #shoot(all_bullets)
		for bullet in bull:
		    for enemy in pygame.sprite.spritecollide(bullet,all_enemy,True):
			    enemy.kill()
			    print(len(all_enemy))
		for enemy in all_enemy:
			enemy.move_forward(3)
			if enemy.rect.y > 1200:
				enemy.rect.y = random.choice(pos2)
		if len(all_enemy) == 0:
			for i in range(3):
				enemy = Ranger(GREEN,120,180,)
				enemy.rect.center =(random.choice(pos),random.choice(pos2))
				all_enemy.add(enemy)
		all_bullets.update()
		print(str(shoot_btn.status()))
		all_sprite_list.update()
		all_sprite_list.draw(screen)
		pygame.display.update()
		clock.tick(60)
if __name__ == '__main__':
			main()
			