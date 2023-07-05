import pygame,sys,random
from config import *
from player import Player
from bowling import Bowling
from invader import Invader

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.icon = pygame.display.set_icon(pygame.image.load("./src/images/icon/icon_1.png").convert())

        self.backgrounds = {'space_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/space.png').convert(), SCREEN_SIZE),
                            'pretty_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/pretty.jpg').convert(), SCREEN_SIZE),
                            'death_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/death.jpg').convert(), SCREEN_SIZE),
                            'squared_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/squared.jpg').convert(), SCREEN_SIZE),
                            'yellow_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/yellow.png').convert(), SCREEN_SIZE)}

        self.png_paths = {'will':'./src/images/player/will.png',
                          'firestar':'./src/images/player/proyectiles/firestar.png',
                          'bowling':'./src/images/enemies/bowling.png',
                          'invader':'./src/images/enemies/space_invader.png',
                          'redball':'./src/iamges/enemies/proyectiles/redball.png'}

        #self.font = []

        self.effect_pngs = {'explosion_1':'./src/images/effects/explosion.png'}

        self.sound_effects = {'fire':pygame.mixer.Sound("./src/sounds/pap.mp3"),
                              'laser':pygame.mixer.Sound("./src/sounds/laser.wav"),
                              'redball':pygame.mixer.Sound("./src/sounds/blublu.wav")}
        #self.music

        player_info = {'score':0, 'hits':0, 'kills':0, 'play_time':0}
        self.player = Player(self.png_paths['will'],PLAYER_SIZE,PLAYER_ORIGIN,self.sound_effects['laser'], player_info)

        self.bowlings = pygame.sprite.Group()

        #SPACE INVADER
        self.firestars = pygame.sprite.Group()
        self.invaders = pygame.sprite.Group()
        self.redballs = pygame.sprite.Group()

        #otro


        #general
        self.sprites = pygame.sprite.Group()
        self.hero = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.proyectiles = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        #assign
        self.sprites.add(self.player)
        self.hero.add(self.player)
        self.enemies.add(self.bowlings)
        self.enemies.add(self.invaders)
        self.proyectiles.add(self.firestars)
        #self.badstacules.add()
        #self.goodstacules.add()

        #game states
        self.running = True
        self.playing = True
        self.pause = False
        self.over = False
        #game selector
        self.space_invaders = True

    def play(self):

        while self.running:
            self.clock.tick(FPS)
            self.event_manage()
            self.update()
            self.render()

    def event_manage(self):
        delay = 7

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            elif self.playing:
                if self.space_invaders:

                    #pygame.time.set_timer(event, 6000, 0)
                    #for invader in self.invaders:
                    #    invader.shot(self.sprites, self.redballs)





                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.player.speedx = -PLAYER_SPEED
                            #print(self.nave.velocidad_x)
                        if event.key == pygame.K_RIGHT:
                            self.player.speedx = PLAYER_SPEED
                        if event.key == pygame.K_UP:
                            self.player.speedy = -PLAYER_SPEED
                        if event.key == pygame.K_DOWN:
                            self.player.speedy = PLAYER_SPEED
                        if event.key == pygame.K_SPACE:
                            self.player.fire_star(self.sprites, self.firestars)
                        if event.key == pygame.K_p:
                            self.stop_sprites()
                            self.pause = True
                            self.playing = False
                        
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and self.player.speedx < 0:
                            self.player.speedx = 0
                        elif event.key == pygame.K_RIGHT and self.player.speedx > 0:
                            self.player.speedx = 0
                        elif event.key == pygame.K_UP and self.player.speedy < 0:
                            self.player.speedy = 0
                        elif event.key == pygame.K_DOWN and self.player.speedy > 0:
                            self.player.speedy = 0
            elif self.pause:
                if self.space_invaders:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.play_sprites()
                            self.playing = True
                            self.pause = False
                        if event.key == pygame.K_r:
                            self.reset_sprites()
                            for firestar in self.firestars:
                                firestar.kill()
                            for invader in self.invaders:
                                invader.kill()
                            for redball in self.redballs:
                                redball.kill()
                            self.playing = True
                            self.pause = False
                        if event.key == pygame.K_s:
                            pass
            elif self.over:
                if self.space_invaders:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.play_sprites()
                            self.playing = True
                            self.over = False

    def update(self):
        if self.space_invaders:
            #offscren kill, collisions doer, enemies spawn, update
            self.border_killer()
            self.collisions_checker()
            self.enemies_maker(False, True)
            self.sprites.update()

    def border_killer(self):
        for enemies in self.enemies:
            if enemies.rect.top >= HEIGHT: enemies.kill()
        if self.space_invaders:
            for firestar in self.firestars:
                if firestar.rect.bottom <= 0: firestar.kill()
            for redball in self.redballs:
                if redball.rect.bottom >= HEIGHT:redball.kill()
        

    def collisions_checker(self):
        if self.space_invaders:
            for firestar in self.firestars:
                invaders_collisions = pygame.sprite.spritecollide(firestar, self.invaders, True)
                redballs_collisions = pygame.sprite.spritecollide(firestar, self.redballs, True)
                if len(invaders_collisions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 10
                    self.player.player_info['kills'] += 1
                if len(redballs_collisions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 5
                    
                    
                    
            player_collisions_invaders = pygame.sprite.spritecollide(self.player, self.invaders, False)
            player_collisions_redballs = pygame.sprite.spritecollide(self.player, self.redballs, False)
            if len(player_collisions_invaders) != 0:
                self.player.player_info['hits'] += 0.1
            if len(player_collisions_redballs) != 0:
                self.player.player_info['hits'] += 0.1

            self.player.life -= self.player.player_info['hits']
            self.player.player_info['hits'] = 0
            if self.player.life <= 0:
                self.stop_sprites()
                self.over = True
                self.playing = False

    def enemies_maker(self, bowling: bool = True, invaders: bool = True):
        if len(self.bowlings) == 0 and bowling:
            for i in range(BOWLING_CAP):
                origin = (random.randrange(65, WIDTH-65), random.randrange(-180, HEIGHT//3))
                bowling = Bowling(self.png_paths['bowling'], BOWLING_SIZE, origin, BOWLING_SPEED)
                self.bowlings.add(bowling)
                self.enemies.add(bowling)
                self.sprites.add(bowling)
        elif len(self.invaders) == 0 and invaders:
            
            y = 85
            for wave in range(INVADER_WAVES):
                for i in range(INVADER_CAP):
                    origin = (random.randrange(20, WIDTH-20), y)
                    invader = Invader(self.png_paths['invader'], self.sound_effects['redball'],INVADER_SIZE, origin, INVADER_SPEED)
                    invader.pilot(self.sprites, self.redballs)
                    self.invaders.add(invader)
                    self.enemies.add(invader)
                    self.sprites.add(invader)
                y += 30
                
            

    def stop_sprites(self):
        for sprite in self.sprites:
            sprite.stop()
    
    def play_sprites(self):
        for sprite in self.sprites:
            sprite.play()

    def reset_sprites(self):
        for sprite in self.sprites:
            sprite.reset()
    
    def kill_sprites(self):
        for sprite in self.sprites:
            sprite.kill()
        

    def reset_sprites(self):
        if self.space_invaders:
            self.player.reset()
            self.invaders.remove()
            
        
    
    def display_text(self, msg: str, size: int, type: str, color: tuple, background: tuple, coord: tuple, display = False):
        font = fonts(size) 
        text = font[type].render(msg, True, color, background)
        text_rect = text.get_rect()
        text_rect.center = coord
        if(display):
            self.screen.blit(text, text_rect)
        return text

    def display_hud(self, show = False):
        if show:
            self.screen.blit(self.backgrounds['space_1'], ORIGIN)

            score_msg = f"score: {int(self.player.player_info['score']):07d}"
            score_sur = self.display_text(score_msg, 24, 'grafitti_regular', PINK, BLACK, SCORE_POS, False)
            score_rect = score_sur.get_rect()
            score_rect.midtop = (SCORE_POS)
            kill_msg = f"kills: {int(self.player.player_info['kills']):07d}"
            kills_sur = self.display_text(kill_msg, 20, 'grafitti_regular', PINK, BLACK, KILLS_POS, False)
            kills_rect = kills_sur.get_rect()
            kills_rect.topright = (WIDTH-15, 15)
            life_msg = f"life: {int(self.player.life)}"
            life_sur = self.display_text(life_msg, 20, 'grafitti_regular', PINK, BLACK, DEATHS_POS, False)
            life_rect = life_sur.get_rect()
            life_rect.topright = (WIDTH-15, 15+kills_rect.height)
            playtime_msg = f"playtime: {(self.player.player_info['play_time'])//1000}"
            playtime_sur = self.display_text(playtime_msg, 18, "elegant_regular", WHITE, BLACK, (WIDTH,HEIGHT//2),False)
            playtime_rect = playtime_sur.get_rect()
            playtime_rect.midright = (WIDTH,HEIGHT//2)

            self.screen.blit(score_sur, score_rect)
            self.screen.blit(kills_sur, kills_rect)
            self.screen.blit(life_sur, life_rect)
            self.screen.blit(playtime_sur, playtime_rect)
    
    def render(self):
        
        if self.playing:
            self.play_sprites()
            self.player.player_info['play_time'] = int(pygame.time.get_ticks())
            self.display_hud(True)
            if self.space_invaders:
                self.sprites.draw(self.screen)
            
        elif self.pause:
            if self.space_invaders:
                pause_screen = pygame.transform.scale(self.backgrounds['yellow_1'], PAUSE_SIZE)
                
                self.screen.blit(pause_screen, (175, 175))
                y = 230
                self.display_text(' |-resume (p)-| ', 24, 'gothic_light', BLACK, (255, 204, 255), (WIDTH//2, y), True)
                y+=48
                self.display_text(' |-restart (r)-| ', 24, 'gothic_light', BLACK, (255, 204, 255), (WIDTH//2, y), True)
                y+=48
                self.display_text(' |-options (o)-| ', 24, 'gothic_light', BLACK, (255, 204, 255), (WIDTH//2, y), True)
                y+=48
                self.display_text(' |-select level (s)-| ', 24, 'gothic_light', BLACK, (255, 204, 255), (WIDTH//2, y), True)
                y+=48
                self.display_text(' |-quit (q)-| ', 24, 'gothic_light', BLACK, (255, 204, 255), (WIDTH//2, y), True)
                y+=48
            
        elif self.over:
            if self.space_invaders:
                self.stop_sprites()
                over_screen = pygame.transform.scale(self.backgrounds['death_1'], SCREEN_SIZE)
                self.screen.blit(over_screen, ORIGIN)
                self.display_text("GAME OVER", 48, 'fancy_titles', RED, BLACK, (WIDTH//2 , HEIGHT//3), True)
                self.display_text("continue? (y)", 48, 'fancy_titles', ORANGE, BLACK, (WIDTH//2 , HEIGHT//2), True)
                
        
        pygame.display.flip()
   
    

        













