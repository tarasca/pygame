import pygame
from config import *

class RedStar(pygame.sprite.Sprite):
    def __init__(
            self,
            path_imagen: str, 
            size: tuple, 
            center: tuple, 
            speed: int = 5, 
            aceleration: float = 1):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(),size)
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.speed_x = 0
        self.speed_y = speed
        self.aceleration = aceleration

    def update(self):
        self.aceleration += 0.1
        self.rect.x += self.speed_x * self.aceleration
        self.rect.y += self.speed_y * self.aceleration

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0