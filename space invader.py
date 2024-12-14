import pygame
 
pygame.init()
# Screen dimensions and title 
WIDTH = 1000
HEIGHT = 650
TITLE = "Space Invader"

#Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#Loading the images 
bg = pygame.image.load("spaceship background.png")
red_ss = pygame.image.load("red spaceship.png")
yllw_ss = pygame.image.load("yellow spaceship.png")


#Resizing the images 
bg = pygame.transform.scale(bg, (1000, 650))
red_ss = pygame.transform.scale(red_ss, (80, 80))
yllw_ss = pygame.transform.scale(yllw_ss, (80, 80))

#Rotating the spaceships
red_ss = pygame.transform.rotate(red_ss, 90)
yllw_ss = pygame.transform.rotate(yllw_ss, 270)

#variables and list
run = True 
red_bullets= []
yllw_bullets = []
r_hp = 10
y_hp = 10
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

#function to draw/move bullets
def move_bullets():
    global y_hp,r_hp
    for red_bullet in red_bullets:
        pygame.draw.rect(screen,"red",red_bullet,0)
        red_bullet.x += 5
        if red_bullet.colliderect(ss_yllw.rect):
            y_hp = y_hp - 1
            red_bullets.remove(red_bullet)
    for yllw_bullet in yllw_bullets:
        pygame.draw.rect(screen,"yellow",yllw_bullet,0)   
        yllw_bullet.x -= 5
        if yllw_bullet.colliderect(ss_red.rect):
            r_hp = r_hp - 1 
            yllw_bullets.remove(yllw_bullet)

       

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
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_f:
                red_bullet = pygame.Rect(ss_red.rect.x + 80,ss_red.rect.y + 40,15,8)
                red_bullets.append(red_bullet)
            if event.key == pygame.K_END:
                yllw_bullet = pygame.Rect(ss_yllw.rect.x - 30,ss_yllw.rect.y + 40,15,8)
                yllw_bullets.append(yllw_bullet)


    #draw background and sprites
    screen.blit(bg, (0, 0))
    pygame.draw.line(screen, "black", (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 20)  # Black line barrier
    gs.draw(screen)

    #move the spaceships
    ss_red.move_red()
    ss_yllw.move_yllw()

    
    #calling the move function   
    move_bullets()


    # writing down hp 
    #red hp
    font = pygame.font.SysFont("Verdana",46)
    text = font.render("Health = "+ str(r_hp),True,"red")
    screen.blit(text,(10,5))
    #yellow hp
    font = pygame.font.SysFont("Verdana",46)
    text = font.render("Health =" + str(y_hp),True,"yellow")
    screen.blit(text,(700,5))
    
    #ending the game
    if y_hp == 0:
        run = False
        #game over text
        font = pygame.font.Sysfont("Verdana",46)
        text = font.render("Game Over, Red wins",True,"White")
        screen.blit(text,(300,325))
        pygame.display.update()
        pygame.time.delay(5000)
        #red
    if r_hp == 0:
        run = False
        #game over text
        font = pygame.font.SysFont("Verdana",46)
        text = font.render("Game Over, Yellow wins",True,"White")
        screen.blit(text,(300,325))
        pygame.display.update()
        pygame.time.delay(5000)
    #update the display
    pygame.display.update()
    #control the frame rate (60 frames per second)
    pygame.time.Clock().tick(60)
    
#Quit the game
pygame.quit()
