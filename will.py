import pygame
from bullet import Bullet
from config import *

class Will(pygame.sprite.Sprite):
    def __init__(
            self, 
            path_image: str,
            size: tuple, 
            midBottom: tuple,
            speed: int, 
            aceleration
        ):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(),size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = midBottom

        self.speed_x = 0
        self.speed_y = 0
        self.aceleration = 1

    def update(self):
        self.rect.x += self.speed_x * self.aceleration
        self.rect.y += self.speed_y * self.aceleration

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def fire(self,image_path: str, sprites, bullets):
        bullet = Bullet(image_path, BULLET_SIZE*3, self.rect.midtop, BULLET_SPEED)
        self.sound_bullet.play()
        sprites.add(bullet)
        bullets.add(bullet)
        

