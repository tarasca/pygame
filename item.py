import pygame,random
from config import *

class Fruit(pygame.sprite.Sprite):
    def __init__(
            self, 
            image_path: str,
            sound: pygame.mixer.Sound,
            size: tuple, 
            center: tuple):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(image_path),size)
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.sound = sound

        self.speedx = 0
        self.speedy = 7
        self.aceleration = 1

        self.playing = True
        
    def update(self):
        if self.playing:
            self.rect.x += self.speedx * self.aceleration
            self.rect.y += self.speedy * self.aceleration
    def stop(self):
        self.playing = False
    def play(self):
        self.playing = True
    