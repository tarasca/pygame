from pygame.font import Font  
#setup screen const
WINDOW_TITLE = "doctor mengueche"

#screen size consts
ORIGIN = (0, 0)
WIDTH = 1000
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)
PAUSE_SIZE = (650, 650)
######################################
UP_LEFT = (0, 0)
UP_CENTER = (WIDTH//2, 0)
UP_RIGHT = (WIDTH, 0)
CENTER_LEFT = (0, HEIGHT//2)
CENTER = (WIDTH//2, HEIGHT//2)
CENTER_RIGTH = (WIDTH, HEIGHT//2)
DOWN_LEFT = (0,HEIGHT)
DOWN_CENTER = (WIDTH//2, HEIGHT) 
DOWN_RIGTH = (WIDTH, HEIGHT)
#fonts
def fonts(size: int):
    fonts = {'elegant_regular':Font('./src/fonts/Agdasima-Regular.ttf',size),
             'elegant_regular':Font('./src/fonts/Agdasima-Bold.ttf',size),
             'fancy_titles':Font('./src/fonts/Nabla-Regular.ttf',size),
             'gothic_bold':Font('./src/fonts/CairoPlay-Bold.ttf',size),
             'gothic_extralight':Font('./src/fonts/CairoPlay-ExtraLight.ttf',size),
             'gothic_light':Font('./src/fonts/CairoPlay-Light.ttf',size),
             'gothic_regular':Font('./src/fonts/CairoPlay-Regular.ttf',size),
             'stdtxt_bold':Font('./src/fonts/RobotoMono-Bold.ttf',size),
             'stdtxt_extralight':Font('./src/fonts/RobotoMono-ExtraLight.ttf',size),
             'stdtxt_medium':Font('./src/fonts/RobotoMono-Medium.ttf',size),
             'stdtxt_regular':Font('./src/fonts/RobotoMono-Regular.ttf',size),
             'stdtxt_semibold':Font('./src/fonts/RobotoMono-SemiBold.ttf',size),
             'stdtxt_thin':Font('./src/fonts/RobotoMono-Thin.ttf',size),
             'grafitti_light':Font('./src/fonts/Tourney-Light.ttf',size),
             'grafitti_regular':Font('./src/fonts/Tourney-Regular.ttf',size),
             'grafitti_medium':Font('./src/fonts/Tourney-Medium.ttf',size),
             'grafitti_bold':Font('./src/fonts/Tourney-Bold.ttf',size)}
    
    return fonts
#refresh rate const
FPS = 60
#colours palet
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
ORANGE = (255, 128, 0)
LIME = (128, 255, 0)
TURQOISE = (0, 255,128)
PURPLE = (128, 255, 0)
FUXSIA= (255, 0 ,128)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#game costs


#Player consts

PLAYER_ORIGIN = (DOWN_CENTER)
PLAYER_SIZE = (70, 70)
PLAYER_SPEED = 15

#hud consts
SCORE_POS = (WIDTH//2, 15)
KILLS_POS = (WIDTH-65, 0)
DEATHS_POS = (WIDTH-70, 16)

#Firestar consts
FIRESTAR_SIZE = (35, 35)
FIRESTAR_SPEED = 13

#Bowling_ball consts
BOWLING_CAP = 12
BOWLING_SIZE = (80, 80)
BOWLING_SPEED = 8

#invaders consts
INVADER_WAVES = 10
INVADER_CAP = 6
INVADER_SIZE = (40,40)
INVADER_SPEED = 4.5
