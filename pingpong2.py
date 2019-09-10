import pygame, random, time
from pygame.locals import *
from datetime import datetime

#--------------- definició de la funció de parada
def parada(pause) :
    pygame.mixer.music.pause()
    while pause:
        for e in pygame.event.get() :
            if e.type == QUIT :
                pygame.quit()
                quit()
            elif e.type == KEYDOWN :
                if e.key == K_ESCAPE :
                    pygame.quit()
                    quit()
                if e.key == K_UP or e.key == K_DOWN or e.key == 119 or e.key == 115  :
                    pause = False
                    pygame.mixer.music.unpause()
        tipo =  pygame.font.SysFont(None, int(amplada/5))
        para = tipo.render("PAUSA", 1, (255, 255, 255))
        fines.blit(para, (amplada/4, alsada/3))
        pygame.display.flip()
    return pause

def two() :
    #------- definició de variables gobals
    amplada, alsada = 900, 750
    centre_x, centre_y = amplada/2, alsada/2
    area = amplada*alsada
    run = True
    pause = False
    #-------- colors principals
    groc, negre, verd, roig = (225, 225, 1), (1, 1, 1), (1, 125, 1), (125, 1, 1)

    #--------- posicions del dos jugadors
    juga1_x = amplada/100+amplada/180
    juga1_y = centre_y-alsada/20
    juga2_x = amplada-amplada*3/100-amplada/180
    juga2_y = centre_y-alsada/20
    bola_x = centre_x
    bola_y = centre_y
    velocitatBola_x, velocitatBola_y, score1, score2 = 3, 3, 0, 0
    moviment = 0
    moviment0 =  0
    direccio = random.randint(1,2)
    if direccio == 1 :
        velocitatBola_y = -velocitatBola_y

    # comença el programa
    pygame.init()
    #--------------- conversió d'imatges
    ball = "ball.png"
    ping_bl = pygame.image.load(ball)
    ping_bl = pygame.transform.scale(ping_bl, (int(amplada/35), int(amplada/35)))
    #--------------- so del ping pong
    ping_so = pygame.mixer.Sound("ping.wav")
    hora = pygame.time.Clock()
    fines = pygame.display.set_mode((amplada, alsada))
    pygame.mixer.music.load("TwoSteps.mp3")
    pygame.mixer.music.play(-1)
    while run :
        change_color1, change_color2 = verd, verd
        if pause == False :
            for events in pygame.event.get() :
                if events.type == QUIT :
                    pygame.quit()
                    quit()
                elif events.type == KEYDOWN :
                    if events.key == K_ESCAPE :
                        pygame.quit()
                        quit()
                    if events.key == K_UP  :
                        moviment -= 5
                    if events.key == K_DOWN  :
                        moviment += 5
                    if events.key == 119 :
                        moviment0 -= 5
                    if events.key == 115 :
                        moviment0 += 5
                    if events.key == 112 :
                        pause = True
                        pause = parada(pause)
                elif events.type == KEYUP :
                    if events.key == K_UP or events.key == K_DOWN :
                        moviment = 0
                    if events.key == 119 or events.key == 115 :
                        moviment0 = 0
            # moviment de la bola
            bola_x += velocitatBola_x
            bola_y += velocitatBola_y
            if  bola_y > alsada/10*9 - amplada/50 or bola_y < alsada/10 + amplada/50 :
                velocitatBola_y = -velocitatBola_y
                pygame.mixer.Sound.play(ping_so)
            if bola_x > amplada - amplada/50 + amplada/50 or bola_x < amplada/100 - amplada/50 :
                if bola_x < centre_x :
                    score2 += 1
                else :
                    score1 += 1
                bola_x = centre_x
                bola_y = centre_y
                velocitatBola_x = -velocitatBola_x
                direccio = random.randint(1,2)
                if direccio == 1 :
                    velocitatBola_y = -velocitatBola_y

            # moviment dels jugadors
            juga2_y += moviment
            if juga2_y < alsada/10 :
                juga2_y = alsada/10
            if juga2_y > alsada/10*9-alsada/10 :
                juga2_y = alsada*9/10-alsada/10
            juga1_y += moviment0
            if juga1_y < alsada/10 :
                juga1_y = alsada/10
            if juga1_y > alsada/10*9-alsada/10 :
                juga1_y = alsada/10*9-alsada/10
        # coalicions de la bola amb els jugadors
        if bola_x +amplada/100 > juga2_x and juga2_y < bola_y +amplada/100 < juga2_y+alsada/10 :
            change_color2 = roig
            direccio = random.randint(1,2)
            if direccio == 1 :
                velocitatBola_y = -velocitatBola_y
            velocitatBola_x = -velocitatBola_x
        if bola_x - amplada/50 < juga1_x+amplada/50 and juga1_y< bola_y - amplada/50 < juga1_y+alsada/10+amplada/50 :
            change_color1 = roig
            direccio = random.randint(1,2)
            if direccio == 1 :
                velocitatBola_y = -velocitatBola_y
            velocitatBola_x = -velocitatBola_x
        fines.fill(groc)
        tipograf  = pygame.font.SysFont(None, int(amplada/10))
        marcador = tipograf.render("JugadorA: {} <> JugadorB: {}".format(score1, score2), 1, roig)
        fines.blit(marcador, (amplada/50, 0))
        pygame.draw.rect(fines, verd, (amplada/100, alsada/10, amplada-amplada/50, alsada/5*4), int(alsada/100))
        pygame.draw.line(fines, verd, [amplada/2, alsada/10], [amplada/2, alsada/10*9], int(alsada/180))
        pygame.draw.circle(fines, verd, (int(centre_x), int(centre_y)), int(amplada/25), int(amplada/220))
        pygame.draw.rect(fines, change_color1, (juga1_x, juga1_y, amplada/50, alsada/10), 0)
        pygame.draw.rect(fines, change_color2, (juga2_x, juga2_y, amplada/50, alsada/10), 0)
        #pygame.draw.circle(fines, roig, (int(bola_x), int(bola_y)), int(amplada/50), 0)
        fines.blit(ping_bl, (bola_x - int(amplada/50), bola_y -  int(amplada/50)))
        if (score1 >= 11 and score1-1>score2) or (score2 >= 11 and score2-1>score1) :
            run = False
            pygame.mixer.music.stop()
            if score1 > score2 :
                final = tipograf.render("Guanyador jugadorA: {} - {}".format(score1, score2), 1, roig)
                fines.blit(final, (amplada/20, alsada/3))
            else :
                final = tipograf.render("Guanyador jugadorB: {} - {}".format(score2, score1), 1, roig)
                fines.blit(final, (amplada/20, alsada/3))            
        pygame.display.flip()
        pygame.display.update()
        hora.tick(350)
        if change_color1 == roig or change_color2 == roig :
            time.sleep(0.5)
        if (score1 >= 11 and score1-1>score2) or (score2 >= 11 and score2-1>score1) :
            time.sleep(2)
   
#------- definició de variables gobals
amplada, alsada = 900, 750
centre_x, centre_y = amplada/2, alsada/2
area = amplada*alsada
run, pause = True, False
#-------- colors principals
groc, negre, verd, roig = (225, 225, 1), (1, 1, 1), (1, 125, 1), (125, 1, 1)

# comença el programa
pygame.init()
#--------------- conversió d'imatges
ball = "ball.png"
ping_bl = pygame.image.load(ball)
ping_bl = pygame.transform.scale(ping_bl, (int(amplada/35), int(amplada/35)))
#--------------- so del ping pong
ping_so = pygame.mixer.Sound("ping.wav")
hora = pygame.time.Clock()
fines = pygame.display.set_mode((amplada, alsada))

