import pygame,random
from config import *

class Bowling(pygame.sprite.Sprite):
    def __init__(self, image_path: str, size: tuple, center: tuple, speed: int = 7):
        super().__init__()

        self.image = self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(),size)
        self.rect = self.image.get_rect() 
        self.rect.center = center

        self.speedx = 0
        self.speedy = speed
        self.aceleration = 1 #(1-2)

        self.playing = True
    def update(self):
        if self.playing:
            self.rect.x += self.speedx * self.aceleration
            self.rect.y += self.speedy * self.aceleration
    def stop(self):
        self.playing = False
    def play(self):
        self.playing = True

    def generate(self,sprites: pygame.sprite.Sprite, enemies: pygame.sprite.Sprite, bowlings: pygame.sprite.Sprite):
        if len(self.bowlings) == 0:
            for i in range(BOWLING_CAP):
                origin = (random.randrange(65, WIDTH-65), random.randrange(-180, HEIGHT//3))
                bowling = Bowling(self.png_paths['bowling'], BOWLING_SIZE, origin, BOWLING_SPEED)
                bowlings.add(bowling)
                enemies.add(bowling)
                sprites.add(bowling)
