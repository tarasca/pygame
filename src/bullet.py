import pygame
from config import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_path: str, size: tuple, midbottom: tuple, speed: int = 7, aceleration: float = 1):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha, size)
        self.rect = self.image.get_rect()
        self.rect.midtop = midbottom

        self.speed_x = speed
        self.speed_y = 0
        self.aceleration = 1.1
        
    def update(self):
        self.aceleration += 0.1
        self.rect.x += self.speed_x * self.aceleration
        self.rect.y -= self.speed_y * self.aceleration

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0