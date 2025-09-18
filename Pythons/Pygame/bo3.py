import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
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
large_text = pygame.font.SysFont("Comicsansms",80)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Create a paddle class
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.color = GREY
        self.rect = pygame.Rect(WIDTH // 2 - self.width // 2, HEIGHT - 30, self.width, self.height)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.width:
            self.rect.x = WIDTH - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Create a ball class
class Ball:
    def __init__(self):
        self.color = WHITE
        self.radius = 10
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, self.radius * 2, self.radius * 2)
        self.velocity = [random.choice([-4, 4]), -4]

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Bounce off walls
        if self.rect.x <= 0 or self.rect.x >= WIDTH - self.radius * 2:
            self.velocity[0] *= -1
        if self.rect.y <= 0:
            self.velocity[1] *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
    def reset(self,x,y):
        self.rect.center =(x,y)
        #self.velocity =[random.choice(-4,4),-4]


# Create a brick class
class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def btn(txt,x,y,width,height,ic,ac,paddle,type=""):
    global left_clicked
    global right_clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0]> x and y + height > mouse[1]>y and click[0] == 1:
        pygame.draw.rect(screen,ac,(x,y,width,height))
        if click[0] == 1 and type == 'left':
            paddle.move(-9)
        elif click[0] == 1 and type =='right':
            paddle.move(9)
            
            
    else:
        clicked = False        
        pygame.draw.rect(screen,ic,(x,y,width,height))
    msg = large_text.render(txt,True,WHITE)
    txt_dim = ((x+(width/2.856)),(y+(height/6.967)))
    screen.blit(msg,txt_dim)

# Main game function
def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    

    # Create bricks
    bricks = []
    brick_width = 75
    brick_height = 20
    for row in range(5):
        for col in range(10):
            brick = Brick(col * (brick_width + 5) + 15, row * (brick_height + 5) + 40, brick_width, brick_height)
            bricks.append(brick)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-8)
        if keys[pygame.K_RIGHT]:
            paddle.move(8)

        # Move the ball
        ball.move()

        # Check for collisions with the paddle
        if ball.rect.colliderect(paddle.rect):
            ball.velocity[1] *= -1  # Bounce off the paddle

        # Check for collisions with bricks
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.velocity[1] *= -1  # Bounce off the brick
                bricks.remove(brick)  # Remove the brick

        # Check for ball falling below the paddle
        if ball.rect.y > HEIGHT:
            print("Game Over!")
           # running = False
            ball.reset(400,300)

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw objects
        for brick in bricks:
            brick.draw(screen)
        paddle.draw(screen)
        ball.draw(screen)
        left_btn = btn("<",75,970,120,65,DRED,RED,paddle,'left')
        right_btn = btn(">",545,970,120,65,DGREEN,GREEN,paddle,'right')

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()