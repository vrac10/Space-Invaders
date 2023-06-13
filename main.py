import pygame 
from spaceship import spaceship
from aliens import Aliens
import random as rd

pygame.init()

clock = pygame.time.Clock()
fps = 60

# bullets  = [pygame.Rect(0+i,0+i,20,20) for i in range(0,4)]



score = 0

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 775
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
current = pygame.time.get_ticks()

bg_img = pygame.image.load("assets/background/background.jpg").convert_alpha()
spaceship_img = pygame.image.load("assets/icons/space.png").convert_alpha()

resized = pygame.transform.scale(spaceship_img, (50, 50))

def bg(surface):
    resized_bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
    surface.blit(resized_bg_img , (0,0))

score_font = pygame.font.Font("assets/font/font.ttf", 24)

alien_image = pygame.image.load("assets/icons/alien.png").convert_alpha()
img = pygame.transform.scale(alien_image,(50,50))

ship = spaceship(250,730)


alien1 = Aliens(40, 90)
alien2 = Aliens(100,90)
alien3 = Aliens(160,90)
alien4 = Aliens(220, 90)
alien5 = Aliens(280,90)
alien6 = Aliens(340,90)
alien7 = Aliens(400,90)
alien8 = Aliens(100,160)
alien9 = Aliens(160,160)
alien10 = Aliens(220, 160)
alien11 = Aliens(280,160)
alien12 = Aliens(340,160)
alien13 = Aliens(160,230)
alien14 = Aliens(220, 230)
alien15 = Aliens(280,230)
alien16 = Aliens(220,300)

aliens = [alien1,alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9,alien10,alien11,alien12,alien13,alien14,alien15,alien16]

def alien_bullet(aliens):
    if len(aliens) >= 2:
        shooters = rd.sample(aliens,2)
    for i in shooters:
        i.shoot(screen,i.alien_bullet_shot)


run = True

while run:

    clock.tick(fps)

    bg(screen)

    #ship.draw(screen)
    ship.draw_bullet(screen,ship.bullet_fired)
    screen.blit(resized, (ship.rect.x - 15 , ship.rect.y - 15 ))

    scores = score_font.render("Score = " + str(score),True,(255,0,0))
    screen.blit(scores,(20,30))
    
    for j in aliens:
        j.draw(screen, img)
 
    for i in aliens:
        i.move()
        ship.bullet_fired,hit = i.collision(ship.bullet, ship.bullet_fired)
        if ship.bullet_fired == False  and hit == True:
            aliens.remove(i)
            score += 1
    

    for i in aliens:
        if i.alien_bullet_shot == True:
            i.bullet.y += 10


    alien_bullet(aliens)

    
   
    ship.move(SCREEN_WIDTH)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if ship.bullet_fired == True:
        if ship.bullet.top + ship.bullet_dy < 0:
            bullet_dy = -ship.bullet.top + 10
            ship.bullet_fired = False
        ship.bullet.y += ship.bullet_dy

    

    pygame.display.update()

pygame.quit()