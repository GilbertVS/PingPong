#_*_ coding utf-8_
"""
"
"@ date: 1 de setembre del 2019
"@ file: Ping.py
"@ description: joc d'hagilitat, taula de ping pong per 1 o 2 jugadors
"@ author: Gilbert Viader
"
"
" importarem les llibreries per usar els seus mètodes de pygame principalment
"
"""
import pygame, random, time
from pygame.locals import *
from datetime import datetime



#---------- definició de sortida del programa
def final() :
    pygame.quit()
    quit()

#--------  definició de la funció esdeveniments
def events() :
    for events in pygame.event.get() :
        if events.type == QUIT :
            final()
        elif events.type == KEYDOWN :
            if events.key == K_ESCAPE :
                final()
        elif events.type == KEYUP:
            pass
                
#------- definició de variables gobals
amplada, alsada = 900, 750
centre_x, centre_y = amplada/2, alsada/2
area = amplada*alsada
#-------- colors principals
groc, negre, verd, roig = (225, 225, 1), (1, 1, 1), (1, 225, 1), (225, 1, 1)
groc1, groc2, groc3 = (225, 225, 1), (225, 225, 1), (225, 225, 1)
verd1, verd2, verd3 = (1, 225, 1), (1, 225, 1), (1, 225, 1)
roig1, roig2, roig3 = (225, 1, 1), (225, 1, 1), (225, 1, 1)
# comença el programa
pygame.init()
hora = pygame.time.Clock()
fines = pygame.display.set_mode((amplada, alsada))
# extreure imatges
pin_portada = pygame.image.load("portada.jpg").convert_alpha()
pin_portada = pygame.transform.scale(pin_portada, (900, 750))
while True :
    events()
    fines.blit(pin_portada, (0,0))
    tipograf = pygame.font.SysFont(None, int(amplada/10))
    retol = tipograf.render("Ping", 1, groc)
    retol2 = tipograf.render("Pong", 1, verd)
    fines.blit(retol, (amplada*0.4, 0))
    fines.blit(retol2, (amplada*0.4+amplada/6, 0))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if amplada*0.4 < mouse[0] < amplada*0.4 + amplada/3 and alsada/8 < mouse[1] < alsada/8 + alsada/5 :
        groc1 = (112, 112, 1)
        verd1 = (1, 112, 1)
        roig1 = (225, 1, 1)
        #if click[0] == 1 or keys[pygame.K_RETURN] :

            
    elif amplada*0.4 < mouse[0] < amplada*0.4 + amplada/3 and alsada/8*3.5 < mouse[1] < alsada/8*3.5 + alsada/5 :
        groc2 = (112, 112, 1)
        verd2 = (1, 112, 1)
        roig2 = (225, 1, 1)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            from pingpong2 import *
            two()
    elif amplada*0.4 < mouse[0] < amplada*0.4 + amplada/3 and alsada/8*6 < mouse[1] < alsada/8*6 + alsada/5 :
        groc3 = (112, 112, 1)
        verd3 = (1, 112, 1)
        roig3 = (225, 1, 1)
        #if click[0] == 1 or keys[pygame.K_RETURN] :

    else :
        groc1, groc2, groc3 = (225, 225, 1), (225, 225, 1), (225, 225, 1)
        verd1, verd2, verd3 = (1, 225, 1), (1, 225, 1), (1, 225, 1)
        roig1, roig2, roig3 = (112, 1, 1), (112, 1, 1), (112, 1, 1)
    pygame.draw.rect(fines, groc1, (amplada*0.4, alsada/8, amplada/3, alsada*0.1), 0)
    pygame.draw.rect(fines, verd1, (amplada*0.4, alsada/8+alsada*0.1, amplada/3, alsada*0.1), 0)
    tipograf2 = pygame.font.SysFont("Serif", int(amplada/15))
    boto1 = tipograf2. render("  1 Jugador", 1, roig1)
    fines.blit(boto1, (amplada*0.4, alsada/8+alsada*0.05))
    pygame.draw.rect(fines, groc2, (amplada*0.4, alsada/8*3.5, amplada/3, alsada*0.1), 0)
    pygame.draw.rect(fines, verd2, (amplada*0.4, alsada/8*3.5+alsada*0.1, amplada/3, alsada*0.1), 0)
    boto2 = tipograf2. render("  2 Jugadors", 1, roig2)
    fines.blit(boto2, (amplada*0.4, alsada/8*3.5+alsada*0.05))
    pygame.draw.rect(fines, groc3, (amplada*0.4, alsada/8*6, amplada/3, alsada*0.1), 0)
    pygame.draw.rect(fines, verd3, (amplada*0.4, alsada/8*6+alsada*0.1, amplada/3, alsada*0.1), 0)
    boto3 = tipograf2. render("  Campionat", 1, roig3)
    fines.blit(boto3, (amplada*0.4, alsada/8*6 +alsada*0.05))
    pygame.display.flip()
    pygame.display.update()
    hora.tick(15)


