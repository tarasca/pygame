#archivo con constantes

#display (en pixeles)
WIDTH = 1000
HEIGHT = 1000
UP_LEFT = (0,0)
UP_CENTER = (WIDTH//2,0)
UP_RIGHT = (WIDTH,0)
CENTER_LEFT = (0,HEIGHT//2)
CENTER = (WIDTH//2,HEIGHT//2)
CENTER_RIGHT = (WIDTH,HEIGHT//2)
DOWN_LEFT = (0,HEIGHT)
DOWN_CENTER = (WIDTH//2,HEIGHT)
DOWN_RIGHT = (WIDTH,HEIGHT)

SCREEN_SIZE = (WIDTH,HEIGHT)
ORIGIN = (0, 0)

ZERO_POS = (0,0)

WILL_SIZE = (50,50)
WILL_SPEED = 10
WILL_ACELERATION = 1
WILL_ORIGIN = ((0+55),HEIGHT)

BULLET_SIZE = (5,25)
BULLET_SPEED = 7

REDSTAR_SIZE = (35,35)
REDSTAR_SPEED = 5
REDSTAR_CAP = 25

#taza de refersco
FPS = 60

#constantes juego
SPEED = 9
BOUNCE = True

#coloretes (rgb ~ red: [0-255] green: [0-255] blue: [0-255] )
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CIAN = (0, 255, 255)
MORADO = (255, 0, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
def custom_color(red:int, green:int, blue:int,print_log=False):
    if((type(red) and type(green) and type(blue)) and 
       ((-1 < red < 256) and (-1 < green < 256) and (-1 < blue < 256))):
        return (red, green, blue)
    else:
        msg = "color code error"
        if(print_log): print(msg)



#fuentes
TEXT_FONTS = \
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria',
'cambriamath', 'candara', 'comicsansms', 'consolas', 'constantia',
'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 
'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 
'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 
'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue',
'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 
'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 
'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 
'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 
'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 
'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsun', 'nsimsun', 
'simsunextb', 'sitkasmall', 'sitkatext', 'sitkasubheading', 'sitkaheading', 
'sitkadisplay', 'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 
'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 
'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 
'yugothicregular', 'yugothicuisemilight', 'holomdl2assets', 'sourcecodeproblack', 'alef', 
'gentiumbasic', 'linuxbiolinumg', 'liberationsans', 'scheherazade', 'davidlibre', 
'notokufiarabic', 'opensymbol', 'liberationmono', 'dejavumathtexgyreregular', 'amiri', 
'caladea', 'sourceserifproblack', 'kacstbook', 'rruehlclm', 'frankruehlclmoblique', 
'frankruehlclmmedium', 'frankruehlclmmediumoblique', 'miriamclm', 'miriamclmbook', 'miriammonoclm', 
'miriammonoclmoblique', 'miriammonoclmbook', 'miriammonoclmbookoblique', 'nachlieliclm', 'nachlieliclmoblique', 
'dejavusans', 'dejavusansoblique', 'dejavusansextralight', 'dejavusanscondensed', 'dejavusanscondensedoblique', 
'dejavusansmono', 'dejavusansmonooblique', 'dejavuserif', 'dejavuserifcondensed', 'gentiumbookbasic', 
'kacstoffice', 'liberationserif', 'linuxbiolinumgregular', 'linuxlibertinegdisplayregular', 'linuxlibertineg', 
'linuxlibertinegsemibold', 'linuxlibertinegregular', 'davidlibreregular', 'frankruhlhofshi', 'frankruhlhofshiregular', 
'miriamlibre', 'miriamlibreregular', 'rubikbold', 'rubik', 'rubikregular', 
'notomono', 'notonaskharabic', 'notonaskharabicui', 'notosans', 'notosanscondensed', 
'notosansregular', 'notosansarabic', 'notosansarabicregular', 'notosansarabicui', 'notosansarabicuiregular', 
'notosansarmenian', 'notosansarmenianregular', 'notosansgeorgian', 'notosansgeorgianregular', 'notosanshebrew', 
'notosanshebrewregular', 'notosanslao', 'notosanslaoregular', 'notosanslisuregular', 'notoserif', 
'notoserifcondensed', 'notoserifregular', 'notoserifarmenian', 'notoserifarmenianregular', 'notoserifgeorgian', 
'notoserifgeorgianregular', 'notoserifhebrew', 'notoserifhebrewregular', 'notoseriflao', 'notoseriflaoregular', 
'sourcecodepro', 'sourcecodeproextralight', 'sourcecodepromedium', 'sourcecodeprosemibold', 'sourcesanspro', 
'sourcesansproextralight', 'sourcesansprosemibold', 'sourceserifpro', 'sourceserifproextralight', 'sourceserifprosemibold', 
'bankgothic', 'bankgothicmedium', 'cityblueprint', 'commercialpi', 'commercialscript', 
'countryblueprint', 'dutch801roman', 'dutch801', 'dutch801extra', 'euroromanoblique', 
'euroroman', 'isocpeur', 'isocteur', 'monospace821', 'panroman', 
'romantic', 'romans', 'sansserifboldoblique', 'sansserif', 'sansserifoblique', 
'stylus', 'superfrench', 'swiss721', 'swiss721outline', 'swiss721condensed', 
'swiss721condensedoutline', 'swiss721blackcondensed', 'swiss721extended', 'swiss721blackextended', 'swiss721black', 
'swiss721blackoutline', 'technicbold', 'techniclite', 'technic', 'universalmath1', 
'vineta', 'acaderef', 'aigdt', 'amdtsymbols', 'amgdt', 
'geniso', 'complex', 'gdt', 'gothice', 'gothicg', 
'gothici', 'greekc', 'greeks', 'isocp2', 'isocp3', 
'isocp', 'isoct2', 'isoct3', 'isoct', 'italicc', 
'italict', '', 'monotxt', 'proxy1', 'proxy2', 
'proxy3', 'proxy4', 'proxy5', 'proxy6', 'proxy7', 
'proxy8', 'proxy9', 'romanc', 'romand', 'romant', 
'scriptc', 'scripts', 'simplex', 'syastro', 'symap', 
'symath', 'symeteo', 'symusic', 'txt']











#desplazamientos
    #efecto bucle, se va por un lado aparece por el otro
#    if(rect_star_1.y >= HEIGHT):
#        rect_star_1.y = 0
#    else:
#        rect_star_1.y += SPEED
#
#   if(rect_star_2.y <= 0):
#        rect_star_2.y = HEIGHT
#    else:
#        rect_star_2.y -= SPEED

    #rebote, es general, se debe cambiar el .y segun corresponda
#    if(BOUNCE): 
#        if(rect_star_3.y < HEIGHT):
#            rect_star_3.y += SPEED
#        else:
#            BOUNCE = False
#    else:
#        if(rect_star_3.y > 0):
#            rect_star_3.y -= SPEED
#        else:
#            BOUNCE = True

#    if(BOUNCE):
#        if(rect_star_4.y > 0):
#            rect_star_4.y -= SPEED
#        else:
#            BOUNCE = False
#    else:
#        if(rect_star_4.y < HEIGHT):
#            rect_star_4.y += SPEED
#        else:
#            BOUNCE = True
    
    #desplazamiento diagonal bucle
#    if(rect_star_5.y >= HEIGHT and rect_star_5.x >= WIDTH):
#        rect_star_5.y = 0
#        rect_star_5.x = 0
#    else:
#        rect_star_5.y += SPEED
#        rect_star_5.x += SPEED
    
#    if(rect_star_6.y <= 0 and rect_star_6.x <= 0):
#        rect_star_6.y = HEIGHT
#        rect_star_6.x = WIDTH
#    else:
#       rect_star_6.y -= SPEED
#       rect_star_6.x -= SPEED

#    if(rect_star_7.y <= 0 and rect_star_7.x >= WIDTH):
#        rect_star_7.y = HEIGHT
#        rect_star_7.x = 0
#    else:
#        rect_star_7.y -= SPEED
#        rect_star_7.x += SPEED
    
#    if(rect_star_8.y >= HEIGHT and rect_star_8.x <= 0):
#        rect_star_8.y = 0
#        rect_star_8.x = WIDTH
#    else:
#        rect_star_8.y += SPEED
#        rect_star_8.x -= SPEED
    
#    if(rect_star_9.x >= WIDTH):
#        rect_star_9.x = 0
#    else:
#        rect_star_9.x += SPEED











































"""
pygame.draw.rect(display,VERDE,(0,0,50,50),1)
pygame.draw.rect(display,VERDE,(50,0,50,50),2)
pygame.draw.rect(display,VERDE,(100,0,50,50),3)
pygame.draw.rect(display,VERDE,(150,0,50,50),4)
pygame.draw.rect(display,VERDE,(200,0,50,50),5)
pygame.draw.rect(display,VERDE,(250,0,50,50),6)
pygame.draw.rect(display,VERDE,(300,0,50,50),7)
pygame.draw.rect(display,VERDE,(350,0,50,50),8)
pygame.draw.rect(display,VERDE,(400,0,50,50),9)
pygame.draw.rect(display,VERDE,(450,0,50,50),10)

pygame.draw.circle(display,AZUL,(25,100),25,1)
pygame.draw.circle(display,AZUL,(75,100),25,2)
pygame.draw.circle(display,AZUL,(125,100),25,3)
pygame.draw.circle(display,AZUL,(175,100),25,4)
pygame.draw.circle(display,AZUL,(225,100),25,5)
pygame.draw.circle(display,AZUL,(275,100),25,6)
pygame.draw.circle(display,AZUL,(325,100),25,7)
pygame.draw.circle(display,AZUL,(375,100),25,8)
pygame.draw.circle(display,AZUL,(425,100),25,9)
pygame.draw.circle(display,AZUL,(475,100),25,10)

pygame.draw.line(display,ROJO,(0,150),(50,150),1)
pygame.draw.line(display,ROJO,(0,150),(50,160),1)
pygame.draw.line(display,ROJO,(0,150),(50,170),1)
pygame.draw.line(display,ROJO,(0,150),(50,180),1)
pygame.draw.line(display,ROJO,(50,150),(100,150),1)
pygame.draw.line(display,ROJO,(50,160),(100,150),1)
pygame.draw.line(display,ROJO,(50,170),(100,150),1)
pygame.draw.line(display,ROJO,(50,180),(100,150),1)

pygame.draw.lines(display,ROJO,True,[(100,250),(150,250),(175,275),(150,300),(100,300),(75,275)])

pygame.draw.ellipse(display,ROJO,(50,350,60,80),1)

pygame.draw.polygon(display,ROJO,[(50,400),(75,450),(82.5,500),(48.5,500),(25,450)])
"""