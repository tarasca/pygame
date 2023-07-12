import pygame,random
from config import *

class Invader(pygame.sprite.Sprite):
    def __init__(self, image_path: list[str],  sound: pygame.mixer.Sound, size: tuple, center: tuple, speed: int = 4) -> None:
        super().__init__()

        #self.clock = 

        self.playing = True

        self.movement = [pygame.transform.scale(pygame.image.load(image_path[0]),size), pygame.transform.scale(pygame.image.load(image_path[1]),size)]
        self.index = 0
        self.image = self.movement[self.index]
        self.rect = self.image.get_rect() 
        self.rect.center = center

        self.sound = sound

        self.speedx = speed
        self.speedy = 0
        self.acceleration = 1
        
    def update(self):
        if self.playing:
            if self.index >= 2:
                self.index = 0
            if self.speedx > 50:
                self.speedx = INVADER_SPEED
            self.rect.x += self.speedx * self.acceleration 
            self.rect.y += self.speedy * self.acceleration
            if self.rect.x <= 0:
                self.rect.x = WIDTH
            elif self.rect.x >= WIDTH:
                self.rect.x = 0  
            self.index = 1
            self.image = self.movement[self.index]
                   

    def shot(self, sprites: pygame.sprite.Sprite, redballs: pygame.sprite.Sprite):
        if self.playing:
            shot = RedBall('./src/images/enemies/proyectiles/redball.png',REDBALL_SIZE, self.rect.midbottom, REDBALL_SPEED)
            self.sound.play()
            sprites.add(shot)
            redballs.add(shot)
            if random.randint(0,1) == 0:
                self.speedx = -self.speedx*1.1
            else: 
                self.speedx = self.speedx*1.1
            #self.acceleration += .01

    

    def stop(self):
        self.playing = False
    def play(self):
        self.playing = True
    def reset(self):
        self.playing = True 

        
class RedBall(pygame.sprite.Sprite):   
    def __init__(self,image_path: str, size: tuple, center: tuple, speed: int = 12):
        super().__init__()
        self.image = self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),size)
        self.rect = self.image.get_rect() 
        self.rect.center = center

        self.speedx = 0
        self.speedy = speed
        self.acceleration = 1.4

        self.playing  = True
    def update(self):
        if self.playing:
            self.rect.x += self.speedx * self.acceleration
            self.rect.y += self.speedy * self.acceleration
    def stop(self):
        self.speedy = 0
    def reset(self):
        self.playing = True
    def play(self):
        self.speedy = 2

    
