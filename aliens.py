import pygame 

class Aliens():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y, 30 , 30)
        self.bullet = pygame.Rect(x+8,y,20,20)
        self.alien_bullet_shot = True
        self.hit = False
        self.timer = pygame.time.get_ticks()
    

    def move(self):
        if self.hit == False:
            if (pygame.time.get_ticks() - self.timer) >= 600:
                if self.rect.x <= self.x:
                    self.timer = pygame.time.get_ticks()
                else:
                    self.rect.x -= 1
            else:
                self.rect.x += 1
    
    def collision(self, bullet, condition):
        if self.rect.colliderect(bullet):
            self.hit = True
            condition = False
        
        return condition,self.hit
        
    def shoot(self,surface, condition):
        if self.hit == False and condition == True:
            pygame.draw.rect(surface,(255,0,0),self.bullet)
            self.alien_bullet_shot = True
            print("hi")
        
    def draw(self,surface,image):
        if self.hit == False:
            #pygame.draw.rect(surface, (255,0,0), self.rect)
            surface.blit(image, (self.rect.x - 10 , self.rect.y - 8))

