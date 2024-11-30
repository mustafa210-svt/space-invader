import pygame 

# Screen dimensions and title 
WIDTH = 1000
HEIGHT = 750 
TITLE = "Space Invader"

#Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#Loading the images 
bg = pygame.image.load("spaceship background.png")
red_ss = pygame.image.load("red spaceship.png")
yllw_ss = pygame.image.load("yellow spaceship.png")

#Resizing the images 
bg = pygame.transform.scale(bg, (1000, 750))
red_ss = pygame.transform.scale(red_ss, (80, 80))
yllw_ss = pygame.transform.scale(yllw_ss, (80, 80))

#Rotating the spaceships
red_ss = pygame.transform.rotate(red_ss, 90)
yllw_ss = pygame.transform.rotate(yllw_ss, 270)

#variables
run = True 

#spaceship class
class Ss(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Function to move the red spaceship 
    def move_red(self):
        key_pressed = pygame.key.get_pressed()
        
        # W key - prevent going out of bounds
        if key_pressed[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 5
        # S key - prevent going out of bounds
        if key_pressed[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += 5
        # A key - prevent crossing the black line
        if key_pressed[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= 5
        # D key - prevent crossing the black line
        if key_pressed[pygame.K_d] and self.rect.right < WIDTH // 2:
            self.rect.x += 5 

    # Function to move the yellow spaceship
    def move_yllw(self):
        key_pressed = pygame.key.get_pressed()

        # Up arrow - prevent going out of bounds
        if key_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        # Down arrow - prevent going out of bounds
        if key_pressed[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5
        # Left arrow - prevent crossing the black line
        if key_pressed[pygame.K_LEFT] and self.rect.left > WIDTH // 2:
            self.rect.x -= 5
        # Right arrow - prevent going out of bounds
        if key_pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

#create spaceship objects
ss_red = Ss(red_ss, 100, 375)
ss_yllw = Ss(yllw_ss, 900, 375)

#group of sprites
gs = pygame.sprite.Group()
gs.add(ss_red)
gs.add(ss_yllw)

#while loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #draw background and sprites
    screen.blit(bg, (0, 0))
    pygame.draw.line(screen, "black", (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 20)  # Black line barrier
    gs.draw(screen)

    #move the spaceships
    ss_red.move_red()
    ss_yllw.move_yllw()

    #update the display
    pygame.display.update()

    #control the frame rate (60 frames per second)
    pygame.time.Clock().tick(60)

#Quit the game
pygame.quit()
