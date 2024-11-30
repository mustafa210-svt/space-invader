import pygame 

#screen dimensions and title 
WIDTH = 1000
HEIGHT = 750 
TITLE = "Space invader"

#setting up the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

#loading the images 
bg = pygame.image.load("spaceship background.png")
red_ss = pygame.image.load("red spaceship.png")
yllw_ss = pygame.image.load("yellow spaceship.png")
#resizing the images 
bg = pygame.transform.scale(bg,(1000,750))
red_ss = pygame.transform.scale(red_ss,(80,80))
yllw_ss = pygame.transform.scale(yllw_ss,(80,80))
#rotating the spaceships
red_ss = pygame.transform.rotate(red_ss,90)
yllw_ss = pygame.transform.rotate(yllw_ss,270)
#variables 
run = True 

#Spaceship class
class Ss(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#object
ss_red = Ss(red_ss,100,375)
ss_yllw = Ss(yllw_ss,900,375)
#group of sprite
gs = pygame.sprite.Group()
gs.add(ss_red)
gs.add(ss_yllw)


#While loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #drawing bg and sprite
    screen.blit(bg,(0,0))
    gs.draw(screen)
    pygame.draw.line(screen,"black",(500,0),(500,750),20)

    pygame.display.update()