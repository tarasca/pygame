import pygame
#from firestar import FireStar
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str,size: tuple, midBottom: tuple, sound: pygame.mixer.Sound, player_info: dict):
        super().__init__()  

        

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = midBottom

        self.sound = sound

        self.speedx = 0
        self.speedy = 0
        self.aceleration = 1

        self.player_info = player_info
        self.life = PLAYER_LIFE
        
        if self.life == 0:
            self.playing = False 
            self.player_info['deaths'] += 1
       
        self.playing = True
    def update(self):
        if self.playing:
            if self.life > PLAYER_LIFE: self.life = PLAYER_LIFE
            self.rect.x += self.speedx * self.aceleration
            self.rect.y += self.speedy * self.aceleration
                
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT

    def fire_star(self, sprites: pygame.sprite.Sprite, firestars: pygame.sprite.Sprite):
        if self.playing:
            firestar = FireStar('./src/images/player/proyectiles/firestar.png',self.rect.midtop,FIRESTAR_SPEED,self.playing)
            self.sound.play()
            sprites.add(firestar)
            firestars.add(firestar)

            

    def stop(self):
        self.playing = False
    def play(self):
        self.playing = True

    def reset(self):
        self.player_info['score'] = 0
        self.player_info['hits'] = 0
        self.player_info['kills'] = 0
        self.player_info['play_time'] = 0
        self.life = 25
        self.playing = True
        self.rect.midbottom = PLAYER_ORIGIN
        self.speedx = 0
        self.speedy = 0
    
class FireStar(pygame.sprite.Sprite):
    def __init__(self,image_path: str, midBottom: tuple, speedy: int = 13, playing: bool = True):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),FIRESTAR_SIZE)
        self.rect = self.image.get_rect() 
        self.rect.midbottom = midBottom

        self.speedy = speedy
        self.speedx = 0

        self.playing = playing

    def update(self):   
        if self.playing:
            self.rect.y -= self.speedy  #up
            #self.rect.y += self.speedy #down
            #self.rect.x -= self.speedx #left
            #self.rect.x += self.speedx #right

    def stop(self):
        self.speedy = 0
    def reset(self):
        self.playing = True
    def play(self):
        self.speedy = FIRESTAR_SPEED