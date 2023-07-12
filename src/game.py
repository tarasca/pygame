import pygame,sys,random,os
from config import *
from player import Player
from bowling import Bowling
from invader import Invader
from item import Fruit

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        #self.time = self.clock.get_time()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.icon = pygame.display.set_icon(pygame.image.load("./src/images/icon/icon_1.png").convert())

        self.backgrounds = {'space_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/space.png').convert(), SCREEN_SIZE),
                            'pretty_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/pretty.jpg').convert(), (840,840)),
                            'death_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/death.jpg').convert(), SCREEN_SIZE),
                            'squared_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/squared.jpg').convert(), SCREEN_SIZE),
                            'yellow_1':pygame.transform.scale(pygame.image.load('./src/images/backgrounds/yellow.png').convert(), SCREEN_SIZE)}

        self.png_paths = {'will':'./src/images/player/will.png',
                          'firestar':'./src/images/player/proyectiles/firestar.png',
                          'bowling':'./src/images/enemies/bowling.png',
                          'invader01':'./src/images/enemies/space_invader01.png',
                          'invader02':'./src/images/enemies/space_invader02.png',
                          'redball':'./src/iamges/enemies/proyectiles/redball.png',
                          'fruit01':'./src/images/items/fruit_1.png'}

        self.fonts = {'elegant_regular':Font('./src/fonts/Agdasima-Regular.ttf',12),
                      'elegant_bold':Font('./src/fonts/Agdasima-Bold.ttf',32),
                      'fancy_titles':Font('./src/fonts/Nabla-Regular.ttf',48),
                      'gothic_bold':Font('./src/fonts/CairoPlay-Bold.ttf',12),
                      'gothic_extralight':Font('./src/fonts/CairoPlay-ExtraLight.ttf',12),
                      'gothic_light':Font('./src/fonts/CairoPlay-Light.ttf',18),
                      'gothic_regular':Font('./src/fonts/CairoPlay-Regular.ttf',12),
                      'stdtxt_bold':Font('./src/fonts/RobotoMono-Bold.ttf',12),
                      'stdtxt_extralight':Font('./src/fonts/RobotoMono-ExtraLight.ttf',32),
                      'stdtxt_medium':Font('./src/fonts/RobotoMono-Medium.ttf',12),
                      'stdtxt_regular':Font('./src/fonts/RobotoMono-Regular.ttf',12),
                      'stdtxt_semibold':Font('./src/fonts/RobotoMono-SemiBold.ttf',12),
                      'stdtxt_thin':Font('./src/fonts/RobotoMono-Thin.ttf',12),
                      'grafitti_light':Font('./src/fonts/Tourney-Light.ttf',12),
                      'grafitti_regular':Font('./src/fonts/Tourney-Regular.ttf',12),
                      'grafitti_medium':Font('./src/fonts/Tourney-Medium.ttf',54),#title
                      'grafitti_bold':Font('./src/fonts/Tourney-Bold.ttf',12)}

        self.effect_pngs = {'explosion_1':'./src/images/effects/explosion.png',
                            'mark_1':'./src/images/effects/mark_1.png'}

        self.sound_effects = {'fire':pygame.mixer.Sound("./src/sounds/pap.mp3"),
                              'laser':pygame.mixer.Sound("./src/sounds/laser.wav"),
                              'redball':pygame.mixer.Sound("./src/sounds/blublu.wav"),
                              'triangle':pygame.mixer.Sound("./src/sounds/pipupi.wav"),
                              'fruit01':pygame.mixer.Sound("./src/sounds/titu.wav")}
        #self.music

        player_info = {'score':0, 'hits':0, 'kills':0, 'play_time':0, 'deaths':0}
        self.player = Player(self.png_paths['will'],PLAYER_SIZE,PLAYER_ORIGIN,self.sound_effects['laser'], player_info)
        self.file_paths = {'root':'./src/main_file.txt',
                           'tmp1':'./src/tmp1_file.txt',
                           'tmp2':'./src/tmp2_file.txt',
                           'tmp3':'./src/tmp3_file.txt'}
        self.file_id = 0

        self.bowlings = pygame.sprite.Group()

        #SPACE INVADER
        self.firestars = pygame.sprite.Group()
        self.invaders = pygame.sprite.Group()
        self.redballs = pygame.sprite.Group()
        self.triangles = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        #otro
        self.score_roof = SCORE_ROOF

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

        self.all_invaders = list()
        self.all_bowlings = list()

        #game states
        self.running = True
        self.playing = False
        self.pause = False
        self.over = False
        self.menu = True
        self.score = False
        #game selector
        self.space_invaders = True
        self.level = 0

    def play(self):

        while self.running:
            self.clock.tick(FPS)
            self.event_manage()
            self.update()
            self.render()

    def event_manage(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            elif self.menu:
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            
                            self.playing = True
                            self.menu = False
                        if event.key == pygame.K_q:
                            self.running = False
                        if event.key == pygame.K_s:
                            self.menu = False
                            self.score = True

                        if event.key == pygame.K_3:
                            pass
                    
            elif self.score:
                
                    if event.type == pygame.K_q:
                        self.menu = True
                        self.score = False


            elif self.playing:
                 
                    prob = random.randint(0,200)
                    if prob >= 185:
                        for fruit in range(1):
                            fruit = Fruit(self.png_paths['fruit01'],self.sound_effects['fruit01'],FRUIT_SIZE,(random.randrange(100,900), 0))
                            fruit.sound.play()
                            self.sprites.add(fruit)
                            self.fruits.add(fruit)


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.player.speedx = -PLAYER_SPEED
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
                    if self.player.player_info['score'] >= self.score_roof:
                        self.stop_sprites()
                        #self.score_roof += 2000
                        if self.level == 0 :
                            
                            with open(self.file_paths['tmp1'], 'w') as tmp_file:
                                tmp_file.write("#####\n")
                                tmp_file.write(f"level = {self.level:1d}\n")
                                tmp_file.write(f"current score = {int(self.player.player_info['score']):06d}\n")
                                tmp_file.write(f"current kills = {int(self.player.player_info['kills']):03d}\n")
                                tmp_file.write(f"damage time = {int(self.player.player_info['hits']):04d}\n")
                                tmp_file.write(f"current deaths = {int(self.player.player_info['deaths']):02d}\n")
                                tmp_file.write(f"current time played = {float(self.player.player_info['play_time'])//1000:04.3f}\n")
                                #tmp_file.write("#####\n")
                                
                            with open(self.file_paths['tmp1'], 'r') as tmp_check:
                                tmp_written = tmp_check.readlines()
                            with open(self.file_paths['root'], 'r') as root_file:
                                root_written = root_file.readlines()

                            if len(tmp_written) != 0:
                                with open(self.file_paths['root'], 'a') as root_file:    
                                    if tmp_written not in root_written:
                                            root_file.writelines(tmp_written)
                                #tmp_file.truncate(0)
                        elif self.level == 1:
                            level_text = self.fonts['stdtxt_extralight'].render("[ Level 02 ]", True, GREEN)
                            level_rect = level_text.get_rect()
                            level_rect.center = CENTER
                            self.screen.blit(level_text, level_rect)
                            with open(self.file_paths['tmp2'], 'w') as tmp_file:
                                tmp_file.write("#####\n")
                                tmp_file.write(f"level = {self.level:1d}\n")
                                tmp_file.write(f"current score = {int(self.player.player_info['score']):06d}\n")
                                tmp_file.write(f"current kills = {int(self.player.player_info['kills']):03d}\n")
                                tmp_file.write(f"damage time = {int(self.player.player_info['hits']):04d}\n")
                                tmp_file.write(f"current deaths = {int(self.player.player_info['deaths']):02d}\n")
                                tmp_file.write(f"current time played = {float(self.player.player_info['play_time'])//1000:04.3f}\n")
                                #tmp_file.write("#####\n")

                            with open(self.file_paths['tmp2'], 'r') as tmp_check:
                                tmp_written = tmp_check.readlines()
                            with open(self.file_paths['root'], 'r') as root_file:
                                root_written = root_file.readlines()

                            if len(tmp_written) != 0:
                                with open(self.file_paths['root'], 'a') as root_file:    
                                    if tmp_written not in root_written:
                                            root_file.writelines(tmp_written)
                                #tmp_file.truncate(0)
                        elif self.level == 2:
                            level_text = self.fonts['stdtxt_extralight'].render("[ Level 03 ]", True, GREEN)
                            level_rect = level_text.get_rect()
                            level_rect.center = CENTER
                            self.screen.blit(level_text, level_rect)
                            with open(self.file_paths['tmp3'], 'w') as tmp_file:
                                tmp_file.write("#####\n")
                                tmp_file.write(f"level = {self.level:1d}\n")
                                tmp_file.write(f"current score = {int(self.player.player_info['score']):06d}\n")
                                tmp_file.write(f"current kills = {int(self.player.player_info['kills']):03d}\n")
                                tmp_file.write(f"damage time = {int(self.player.player_info['hits']):04d}\n")
                                tmp_file.write(f"current deaths = {int(self.player.player_info['deaths']):02d}\n")
                                tmp_file.write(f"current time played = {float(self.player.player_info['play_time'])//1000:04.3f}\n")
                                tmp_file.write(f"id:{self.file_id:06d}\n")
                                #tmp_file.write("#####\n")
                                

                            with open(self.file_paths['tmp3'], 'r') as tmp_check:
                                tmp_written = tmp_check.readlines()
                            with open(self.file_paths['root'], 'r') as root_file:
                                root_written = root_file.readlines()

                            if len(tmp_written) != 0:
                                with open(self.file_paths['root'], 'a') as root_file:    
                                    if tmp_written not in root_written:
                                            root_file.writelines(tmp_written)
                                #tmp_file.truncate(0)
                            
                        self.file_id+=1
                        self.reset_sprites()
                        self.level += 1

                    
                        
                                
                                    


                        
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
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.play_sprites()
                            self.playing = True
                            self.pause = False
                        if event.key == pygame.K_r:
                            self.reset_sprites()
                            for firestar in self.firestars:
                                firestar.kill()
                            for bowling in self.bowlings:
                                bowling.kill()
                            for invader in self.invaders:
                                invader.kill()
                            for redball in self.redballs:
                                redball.kill()
                            self.playing = True
                            self.pause = False
                        if event.key == pygame.K_q:
                            self.menu = True
                            self.pause = False
                            self.reset_sprites()
                            for redball in self.redballs:
                                redball.kill()
                            for fruit in self.fruits:
                                fruit.kill()
                            self.level = 0
                            pygame.time.wait(500)
            elif self.over:
                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.playing = True
                            self.over = False
                            self.reset_sprites()

    def update(self):
        if self.space_invaders:
            #offscren kill, collisions doer, enemies spawn, update
            self.border_killer()
            self.collisions_checker()
            self.enemies_maker()
            self.sprites.update()

    def border_killer(self):
        #for enemies in self.enemies:
         #   if enemies.rect.top >= HEIGHT: enemies.kill()
          #  elif enemies.rect.right >= WIDTH: enemies.kill()
           # elif enemies.rect.left <= 0: enemies.kill()
            #elif enemies.rect.bottom <= 0: enemies.kill()
        if self.space_invaders:
            for firestar in self.firestars:
                if firestar.rect.bottom <= 0: firestar.kill()
            for redball in self.redballs:
                if redball.rect.bottom >= HEIGHT:redball.kill()
            for bowling in self.bowlings:
                if bowling.rect.top >= HEIGHT:bowling.kill()
            for triangle in self.triangles:
                if triangle.rect.left >= WIDTH:triangle.kill()
                if triangle.rect.top >= HEIGHT:triangle.kill()
            for fruit in self.fruits:
                if fruit.rect.top >= HEIGHT:fruit.kill()
        

    def collisions_checker(self):
        if self.space_invaders:
            for firestar in self.firestars:
                invaders_collisions = pygame.sprite.spritecollide(firestar, self.invaders, True)
                redballs_collisions = pygame.sprite.spritecollide(firestar, self.redballs, True)
                bowlings_collitions = pygame.sprite.spritecollide(firestar, self.bowlings, True)
                triangles_collitions = pygame.sprite.spritecollide(firestar, self.triangles, True)
                if len(invaders_collisions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 100
                    self.player.player_info['kills'] += 1
                if len(bowlings_collitions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 75
                    self.player.player_info['kills'] += 1
                if len(redballs_collisions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 50
                if len(triangles_collitions) != 0:
                    firestar.kill()
                    self.player.player_info['score'] += 50
                       
            player_collisions_invaders = pygame.sprite.spritecollide(self.player, self.invaders, False)
            player_collisions_redballs = pygame.sprite.spritecollide(self.player, self.redballs, False)
            player_collisions_bowlings = pygame.sprite.spritecollide(self.player, self.bowlings, False)
            player_collisions_triangles = pygame.sprite.spritecollide(self.player, self.triangles, False)
            player_collisions_fruits = pygame.sprite.spritecollide(self.player, self.fruits, False)
            
            if len(player_collisions_invaders) != 0:
                self.player.player_info['hits'] += 0.1
            if len(player_collisions_redballs) != 0:
                self.player.player_info['hits'] += 0.1
            if len(player_collisions_bowlings) != 0:
                self.player.player_info['hits'] += 0.1
            if len(player_collisions_triangles) != 0:
                self.player.player_info['hits'] += 0.1
            if len(player_collisions_fruits) != 0:
                self.player.life += 5

            self.player.life -= self.player.player_info['hits']
            self.player.player_info['hits'] = 0
            if self.player.life <= 0:
                self.stop_sprites()
                self.over = True
                self.playing = False

    def enemies_maker(self):
        
        if self.playing:
            if self.level == 0:
                for inv in self.all_invaders:
                    if random.randint(0,250) == 1:
                        inv.shot(self.sprites, self.redballs)

                if len(self.invaders) == 0 and self.space_invaders:
                    y = 85
                    for wave in range(3):
                        for i in range(5):
                            if i % 2 == 0:index = -1
                            else:index = 1
                            origin = (random.randrange(20, WIDTH-20), y)
                            invader = Invader([self.png_paths['invader01'], self.png_paths['invader02']], self.sound_effects['redball'],INVADER_SIZE, origin, (INVADER_SPEED*index))
                            
                            self.invaders.add(invader)
                            self.enemies.add(invader)
                            self.sprites.add(invader)
                            self.all_invaders.append(invader)
                            
                        y += 50
                
            elif self.level == 1:
                for bowl in self.all_bowlings:
                    if pygame.time.get_ticks() % 3 == 0:
                        pass
                        #bowl.shot(self.sprites, self.triangles)

                if len(self.bowlings) == 0:
                    for i in range(16):
                        origin = (random.randrange(65, WIDTH-65), random.randrange(-180, HEIGHT//3))
                        bowling = Bowling(self.png_paths['bowling'], self.sound_effects['triangle'], BOWLING_SIZE, origin, 9.5)
                        self.bowlings.add(bowling)
                        self.enemies.add(bowling)
                        self.sprites.add(bowling)
                        self.all_bowlings.append(bowling)
            elif self.level == 2:
                for inv in self.all_invaders:
                        prob = random.randint(0,250)
                        if prob == 0:
                            inv.shot(self.sprites, self.redballs)
                if len(self.bowlings) == 0:
                    for i in range(7):
                        origin = (random.randrange(65, WIDTH-65), random.randrange(-180, HEIGHT//3))
                        bowling = Bowling(self.png_paths['bowling'], self.sound_effects['triangle'], BOWLING_SIZE, origin, 9.5)
                        self.bowlings.add(bowling)
                        self.enemies.add(bowling)
                        self.sprites.add(bowling)
                        self.all_bowlings.append(bowling)

                if len(self.invaders) == 0 and self.space_invaders:
                    y = 85
                    for wave in range(5):
                        for i in range(10):
                            if i % 2 == 0:index = -1
                            else:index = 1
                            origin = (random.randrange(20, WIDTH-20), y)
                            invader = Invader([self.png_paths['invader01'], self.png_paths['invader02']], self.sound_effects['redball'],INVADER_SIZE, origin, (INVADER_SPEED*index))
                            #pygame.time.set_timer(pygame.event.Event(-1, {'':}), random.randrange((3,7)*1000), 10)
                            
                            self.invaders.add(invader)
                            self.enemies.add(invader)
                            self.sprites.add(invader)
                            self.all_invaders.append(invader)
                            
                        y += 50
            elif self.level == 3:
                self.menu = True
                self.pause = False
                self.reset_sprites()
                for redball in self.redballs:
                    redball.kill()
                for fruit in self.fruits:
                    fruit.kill()
                self.level = 0
                pygame.time.wait(500)
            

                
            

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
            for enemies in self.enemies:
                enemies.kill()
           
            
        
    
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
            playtime_msg = f"playtime: {(self.player.player_info['play_time'])/1000:3.2f} segs"
            playtime_sur = self.display_text(playtime_msg, 18, "elegant_regular", WHITE, BLACK, (WIDTH,HEIGHT//2),False)
            playtime_rect = playtime_sur.get_rect()
            playtime_rect.midright = (WIDTH,HEIGHT//2)
            
            self.screen.blit(score_sur, score_rect)
            self.screen.blit(kills_sur, kills_rect)
            self.screen.blit(life_sur, life_rect)
            self.screen.blit(playtime_sur, playtime_rect)
    
    def render(self):
        
        if self.playing:
            self.screen.blit(self.backgrounds['space_1'],ORIGIN)
            self.player.player_info['play_time'] += int(self.clock.get_time())
            self.player.player_info['score'] += (int(self.clock.get_time())/1000)
            self.play_sprites()
            self.display_hud(True)
            if self.level == 0:
                level_text = self.fonts['stdtxt_extralight'].render("[ Level 01 ]", True, GREEN)
                level_rect = level_text.get_rect()
                level_rect.topleft = UP_LEFT
            elif self.level == 1:
                level_text = self.fonts['stdtxt_extralight'].render("[ Level 02 ]", True, GREEN)
                level_rect = level_text.get_rect()
                level_rect.topleft = UP_LEFT
            elif self.level == 2:
                level_text = self.fonts['stdtxt_extralight'].render("[ Level 03 ]", True, GREEN)
                level_rect = level_text.get_rect()
                level_rect.topleft = UP_LEFT
        
            self.screen.blit(level_text, level_rect)
            if self.space_invaders:
                self.sprites.draw(self.screen)

        elif self.score:
            self.screen.blit(self.backgrounds['pretty_1'] , (80, 80))
            y = 0
            x = 0
            n = 0
            with open(self.file_paths['root'],'r') as score_file:
                raw_data = score_file.readlines()
                raw_lines = []
                for line in raw_data:
                    text = self.fonts['gothic_extralight'].render(line,True,GREEN,BLACK)
                    raw_lines.append(text)
                for line in raw_lines:
                    line_rect = line.get_rect()
                    line_rect.topleft = (85+x, 85+y)
                    self.screen.blit(line, line_rect)
                    n += 1
                    if n % 22 == 0:
                        x += 200
                        y = 0
                    y+=22


        elif self.menu:
            if self.space_invaders:
                #background
                self.screen.blit(self.backgrounds['squared_1'],ORIGIN)
                #menu mark
                self.screen.blit(pygame.transform.scale(pygame.image.load(self.effect_pngs['mark_1']).convert_alpha(), (WIDTH-300,HEIGHT-160)), (150,80))
                #menu text
                title_text = self.fonts['grafitti_medium'].render("WILL INVADER'S", True, TITLE_COLOR)
                title_rect = title_text.get_rect()
                title_rect.center = (WIDTH//2, HEIGHT//5.5)
                self.screen.blit(title_text, title_rect)
                #foot page
                #foot_page = self.fonts['gothic_light'].render("by plof",True, (255, 160, 122))
                #footPage_rect = foot_page.get_rect()
                #footPage_rect.topright = title_rect.bottomright
                #self.screen.blit(foot_page, footPage_rect)
                #options body
                options_body = pygame.surface.Surface((450, 450), pygame.SRCALPHA)
                optionsBody_rect = options_body.fill((134, 134, 134 , 150)) 
                optionsBody_rect.center = CENTER
                self.screen.blit(options_body, optionsBody_rect)
                
                option1_body = pygame.surface.Surface((200, 70))
                option1Body_rect = option1_body.fill((119,136,153))
                option1Body_rect.center = (WIDTH//2, 330)
                self.screen.blit(option1_body, option1Body_rect)

                option1_text = self.fonts['elegant_bold'].render("Start", True, (188,143,143))
                option1_rect = option1_text.get_rect()
                option1_rect.center = option1Body_rect.center
                self.screen.blit(option1_text, option1_rect)

                option2_body = pygame.surface.Surface((200, 70))
                option2Body_rect = option2_body.fill((119,136,153))
                option2Body_rect.center = (WIDTH//2, 410)
                self.screen.blit(option2_body, option2Body_rect)

                option2_text = self.fonts['elegant_bold'].render("Options", True, (188,143,143))
                option2_rect = option2_text.get_rect()
                option2_rect.center = option2Body_rect.center
                self.screen.blit(option2_text, option2_rect)
                
                option3_body = pygame.surface.Surface((200, 70))
                option3Body_rect = option3_body.fill((119,136,153))
                option3Body_rect.center = (WIDTH//2, 490)
                self.screen.blit(option3_body, option3Body_rect)

                option3_text = self.fonts['elegant_bold'].render("Score", True, (188,143,143))
                option3_rect = option3_text.get_rect()
                option3_rect.center = option3Body_rect.center
                self.screen.blit(option3_text, option3_rect)

                option4_body = pygame.surface.Surface((200, 70))
                option4Body_rect = option4_body.fill((119,136,153))
                option4Body_rect.center = (WIDTH//2, 570)
                self.screen.blit(option4_body, option4Body_rect)

                option4_text = self.fonts['elegant_bold'].render("Quit", True, (188,143,143))
                option4_rect = option4_text.get_rect()
                option4_rect.center = option4Body_rect.center
                self.screen.blit(option4_text, option4_rect)
                
            
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
                #self.stop_sprites()
                over_screen = pygame.transform.scale(self.backgrounds['death_1'], SCREEN_SIZE)
                self.screen.blit(over_screen, ORIGIN)
                self.display_text("GAME OVER", 48, 'fancy_titles', RED, BLACK, (WIDTH//2 , HEIGHT//3), True)
                
                continue_text = self.fonts['fancy_titles'].render("continue? (space)", True, BLACK, WHITE)
                continue_rect = continue_text.get_rect()
                continue_rect.center = (WIDTH//2 , HEIGHT//2)
                self.screen.blit(continue_text, continue_rect)
                #self.display_text("continue? (space)", 48, 'fancy_titles', BLACK, WHITE, (WIDTH//2 , HEIGHT//2), True)
                
        
        pygame.display.flip()
   
    

        













