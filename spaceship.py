import pygame

class spaceship():
    def __init__(self, x , y):
        self.rect = pygame.Rect(x, y , 20 , 20)
        self.bullet = pygame.Rect(x+8,y,2,20)
        self.bullet_fired = False
        self.bullet_dy = 0
    

    def move(self, screen_width):
        speed = 6
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            dx = speed
        elif key[pygame.K_LEFT]:
            dx = -speed
        elif key[pygame.K_SPACE] and self.bullet_fired == False:
            self.bullet_dy = -5
            self.bullet.x = self.rect.x + 8
            self.bullet.y = self.rect.y
            self.bullet_fired = True

            
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        self.rect.x += dx
        self.rect.y += dy


    def draw_bullet(self,surface,condition):
        if condition == True:
            pygame.draw.rect(surface , (255,0,0), self.bullet)


    # def draw(self, surface):
    #     pygame.draw.rect(surface , (255,0,0), self.rect)
        
       
        
        