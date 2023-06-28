import pygame,sys,random

from config import *
from will import Will
from redstar import RedStar

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_screen = pygame.display.set_mode(SCREEN_SIZE)
        self.game_background = pygame.transform.scale(
            pygame.image.load("./src/images/background_1.jpg").convert, SCREEN_SIZE)
        #self.font
        self.score = 0
        #self.lives

        self.sprites = pygame.sprite.Group()
        self.redstars = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        self.will = Will("./src/images/will.png", WILL_SIZE, WILL_ORIGIN, WILL_SPEED, WILL_ACELERATION)

        self.sprites.add(self.will)
        
        self.playing = False
        self.pause = False
        self.over = False
        self.running = False

    def play(self):
        self.playing = True
        self.running = True

        while self.running:
            self.clock.tick(FPS)
            self.event_manage()
            self.update()
            self.render()

        self.start_screen

    def event_manage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quit window
                pygame.quit()
                sys.exit

            if event.type == pygame.KEYDOWN:#pressed
                if event.key == pygame.K_LEFT:
                    self.will.speed_x = -WILL_SPEED
                if event.key == pygame.K_RIGHT:
                    self.will.speed_x = WILL_SPEED
                if event.key == pygame.K_UP:
                    self.will.speed_y = -WILL_SPEED
                if event.key == pygame.K_DOWN:
                    self.will.speed_y = WILL_SPEED
                if event.key == pygame.K_SPACE:
                    self.will.fire("./src/iamnges/ball", self.sprites, self.lasers)
            
            if event.type == pygame.KEYUP:#not pressed
                if event.key == pygame.K_LEFT and self.will.speed_x < 0:
                    self.will.speed_x = 0
                elif event.key == pygame.K_RIGHT and self.will.speed_x > 0:
                    self.will.speed_x = 0
                elif event.key == pygame.K_UP and self.will.speed_y < 0:
                    self.will.speed_y = 0
                elif event.key == pygame.K_DOWN and self.will.speed_y > 0:
                    self.will.speed_y = 0   

    def update(self):
        self.trash_sprites()
        self.detect_collision()
        self.spawn_redstars()
        self.sprites.update()

    def render(self):
        #juego / menu / pausa config

        if self.playing:
            self.game_screen.blit(self.game_background, ORIGIN)
            self.sprites.draw(self.game_screen)
        elif self.pause:
            self.pause_menu()
        elif self.over:
            self.game_over()

def spawn_redstars(self):
    if len(self.redstars) == 0:
        for i in range(REDSTAR_CAP):
            star_location = (random.randrange(20, WIDTH - 20), 
                             random.randrange(-500, HEIGHT//2))
            redstar = RedStar("./src/images/star_1.png",REDSTAR_SIZE,
                              star_location,REDSTAR_SPEED)
            self.redstars.add(redstar)
            self.sprites.add(redstar)

def stop_sprites(self):
    for sprite in self.sprites:
        sprite.stop()

def detect_collision(self):
    for bullet in self.bullets:
        bullet_collisions = pygame.sprite.spritecollide(bullet, self.redstars, True)
        if len(bullet_collisions) != 0:
            bullet.kill()
        
    will_collisions = pygame.sprite.spritecollide(self.will, self.redstars, False)
    if len(will_collisions) != 0:
        self.stop_sprites()
        self.game_over()




























































































