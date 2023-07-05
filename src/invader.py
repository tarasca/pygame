import pygame
from config import *

class Invader(pygame.sprite.Sprite):
    def __init__(self, image_path: str,  sound: pygame.mixer.Sound, size: tuple, center: tuple, speed: int = 4) -> None:
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),size)
        self.rect = self.image.get_rect() 
        self.rect.center = center

        self.sound = sound

        self.speedx = speed
        self.speedy = 0
        self.acceleration = 1
        
        self.playing = True
        if self.playing:
            time = pygame.time.Clock()
            self.time = time.get_time()
        #self.attack = False
    def update(self):
        if self.playing:
            self.rect.x += self.speedx * self.acceleration
            self.rect.y += self.speedy * self.acceleration
            if self.rect.x <= 0:
                self.rect.x = WIDTH
            elif self.rect.x >= WIDTH:
                self.rect.x = 0

    def pilot(self, sprites: pygame.sprite.Sprite, redballs: pygame.sprite.Sprite):
        if self.playing:
            if self.time %10 == 0:
                shot = RedBall('./src/images/enemies/proyectiles/redball.png',(20,20), self.rect.midbottom, 3)
                self.sound.play()
                sprites.add(shot)
                redballs.add(shot)
                
        
            

    def shot(self, sprites: pygame.sprite.Sprite, redballs: pygame.sprite.Sprite):
        if self.playing:
            shot = RedBall('./src/images/enemies/proyectiles/redball.png',(20,20), self.rect.midbottom, 3)
            self.sound.play()
            sprites.add(shot)
            redballs.add(shot)

    def stop(self):
        self.playing = False
    def play(self):
        self.playing = True
    def reset(self):
        self.playing = True 

        
class RedBall(pygame.sprite.Sprite):   
    def __init__(self,image_path: str, size: tuple, center: tuple, speed: int = 2):
        super().__init__()
        self.image = self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),size)
        self.rect = self.image.get_rect() 
        self.rect.center = center

        self.speedx = 0
        self.speedy = speed
        
        self.acceleration = 1

        self.playing  = True
    def update(self):
        if self.playing:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
    def stop(self):
        self.speedy = 0
    def reset(self):
        self.playing = True
    def play(self):
        self.speedy = 2

    
