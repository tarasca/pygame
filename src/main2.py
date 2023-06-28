import pygame,sys,random
from config import *
from will import Will
from redstar import Knife

def generate_knifes(g_sprites, g_knifes, screen: pygame.Surface, count:int=15):
    if len(g_knifes) == 0:
        for i in range(count):
            x = random.randrange(40,screen.get_width()-40)
            y = random.randrange(-500,screen.get_height()//2)
            knife = Knife("./src/images/knife_1.png",REDSTAR_SIZE,(x,y),REDSTAR_SPEED)
            g_knifes.add(knife)
            g_sprites.add(knife)

#inicia
pygame.init()
#clock
clock = pygame.time.Clock()
#pantalla
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#titulo ventana
pygame.display.set_caption("pygame")
#fondo y efectos
fondo = pygame.image.load('./src/images/fondo_1.jpg').convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

#image_explode = pygame.transform.scale(pygame.image.load('./src/images/explosion_1.png').convert_alpha(),(70,70))
image_bullet = pygame.transform.scale(pygame.image.load('./src/images/bullet_1.png').convert_alpha(),BULLET_SIZE)


#texto
std_font = pygame.font.SysFont('rage',36)#fuente y size
pimba_msg = std_font.render("pimba",True,AMARILLO)#tipeo mensaje

#sonido
sound_collision = pygame.mixer.Sound("./src/sounds/pum.mp3")
sound_bullet = pygame.mixer.Sound('./src/sounds/shot.mp3')

#sprites
sprites = pygame.sprite.Group()
knifes = pygame.sprite.Group()
bullets = pygame.sprite.Group()

#surfaces y rects
will = Will('./src/images/will.png',WILL_SIZE,CENTER,sound_bullet,image_bullet)
sprites.add(will)

while True:#bucle juego
    
    clock.tick(FPS)


    for event in pygame.event.get():#gestion de eventos
        
        if(event.type == pygame.QUIT): 
            pygame.quit()
            sys.exit()
        
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                print("principal", event.pos)
            if(event.button == 2):
                print("medio")
            if(event.button == 3):
                print("secundario")
            if(event.button == 4):
                print("scroll arriba")
            if(event.button == 5):
                print("scroll abajo")

        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                will.speed_x = -WILL_SPEED
            if(event.key == pygame.K_RIGHT):
                will.speed_x = WILL_SPEED
            if(event.key == pygame.K_UP):
                will.speed_y = -WILL_SPEED
            if(event.key == pygame.K_DOWN):
                will.speed_y = WILL_SPEED
            if(event.type == pygame.K_x):
                will.fire(sprites,bullets)

        elif(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT):
                will.speed_x = 0
            if(event.key == pygame.K_RIGHT):
                will.speed_x = 0
            if(event.key == pygame.K_UP):
                will.speed_y = 0
            if(event.key == pygame.K_DOWN):
                will.speed_y = 0

    if will.rect.left <= 0: will.rect.left = 0
    elif will.rect.right >= WIDTH: will.rect.right = WIDTH 
    elif will.rect.top <= 0: will.rect.top = 0
    elif will.rect.bottom >= HEIGHT: will.rect.bottom = HEIGHT

    for knife in knifes:
        if(knife.rect.top >= HEIGHT):
            knife.kill()

    generate_knifes(sprites,knifes,screen,59)

    sprites.update()

    screen.blit(fondo, ZERO_POS)

    pygame.draw.line(screen,MORADO,(WIDTH//2,0),(WIDTH//2,HEIGHT))
    pygame.draw.line(screen,MORADO,(0,HEIGHT//2),(WIDTH,HEIGHT//2))
    
    sprites.draw(screen)

    #colisiones
    
    



    

    pygame.display.flip()
    