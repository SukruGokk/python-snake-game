"""

@author: Şükrü Erdem Gök
@date:start(6/5/2020), finish(7/5/2020)

"""
#LIBS
import pygame
import random as rd
import datetime

#INITITALIZE THE PYGAME
pygame.init()

pygame.mixer.music.load("data\\sound\\Snake.wav")
pygame.mixer.music.play(-1)

#MENU
width=950
height=630

wn=pygame.display.set_mode((width,height))

#HELPER FUNCTION
def textObj(msg,font,r,g,b):
   text=font.render(msg,True,(r,g,b)) 
   return text,text.get_rect()

#MAIN TEXT FUNCTION
def msg(msg,size,x,y,r,g,b):
    font=pygame.font.Font("freesansbold.ttf",size)
    text,textRect=textObj(msg,font,r,g,b)
    textRect.center=(x,y)
    wn.blit(text,textRect)

menuBg=pygame.image.load("data\\img\\menuBg.jpg")
menuRect=menuBg.get_rect()
menuRect.x, menuRect.y=(0,0)

play=pygame.image.load("data\\img\\play.png")
playR=play.get_rect()
playR.x, playR.y=(200,20)

about=pygame.image.load("data\\img\\about.png")
aboutR=about.get_rect()
aboutR.x, aboutR.y=(200,235)

opt=pygame.image.load("data\\img\\options.png")
optR=opt.get_rect()
optR.x, optR.y=(200,440)

info=pygame.image.load("data\\img\\info.jpg")
infoR=opt.get_rect()
infoR.x, infoR.y=(150,300)

lowS=pygame.image.load("data\\img\\Lspeed.png")
lowsR=lowS.get_rect()
lowsR.x, lowsR.y=(300,100)

highS=pygame.image.load("data\\img\\Hspeed.png")
highsR=highS.get_rect()
highsR.x, highsR.y=(300,300)

info=pygame.image.load("data\\img\\info.jpg")
infoR=opt.get_rect()
infoR.x, infoR.y=(150,300)

save=pygame.image.load("data\\img\\save.png")
saveR=save.get_rect()
saveR.x, saveR.y=(261,540)

menu=1
pygame.display.set_caption("RAINBOW SNAKE")

#FPS
clock=pygame.time.Clock()

loopCont=0

speed=10
Nspeed=speed
Hspeed=20

def menuF(menu1):
   
    global speed
    global Nspeed
    global Hspeed
    
    while menu1:
       
        if not (pygame.mixer.music.get_busy()):
          pygame.mixer.music.load("data\\sound\\Snake.wav")
          pygame.mixer.music.play(-1)
        #MENU
        width=950
        height=630
        
        wn=pygame.display.set_mode((width,height))
        
        wn.blit(menuBg, menuRect)
        wn.blit(play,playR)
        wn.blit(about,aboutR)
        wn.blit(opt,optR)
    
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                pygame.quit()
           if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if playR.collidepoint(x,y):
                    menu1=0              
                elif aboutR.collidepoint(x,y):
                    a=1
                    while (a):
                        wn.fill((255,255,255))
                        wn.blit(info,infoR)
                        msg("CREATOR: ŞÜKRÜ ERDEM GÖK",30,450,230,0,0,0)
                        msg("DATE: 6/5/2020 - 7/5/2020",30,450,260,0,0,0)
                        msg("PROGRAMMING LANGUAGE: PYTHON",30,450,290,0,0,0)
                        msg("Click to pass",10,30,10,0,0,0)
                        pygame.display.flip()
                        for event in pygame.event.get():
                           if event.type==pygame.MOUSEBUTTONDOWN:
                                a=0
                           if event.type==pygame.QUIT:
                                pygame.quit()
                        clock.tick(100)
                            
                elif optR.collidepoint(x,y):
                    opti=1
                    while opti:
                        wn.blit(menuBg,menuRect)
                        wn.blit(lowS,lowsR)
                        wn.blit(highS,highsR)
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                x,y=event.pos
                                if lowsR.collidepoint(x,y):
                                    speed=10
                                    Nspeed=speed
                                    Hspeed=20
                                    opti=0
                                elif highsR.collidepoint(x,y):
                                    speed=20
                                    Nspeed=speed
                                    Hspeed=30
                                    opti=0
                        pygame.display.flip()
                    
        pygame.display.flip()

menuF(1)
loopCont=1

#GRASS IMAGE
bg = pygame.image.load("data\\img\\grass.jpg")
rect = bg.get_rect()
rect.x,rect.y = (0,0)

#REPLAY IMAGE
rp = pygame.image.load("data\\img\\tryA.png")
rpRect = rp.get_rect()
rpRect.x , rpRect.y = (25,300)

#SCORE
score=0

#SNAKE'S PIECES
snake=[]

#CREATE SNAKE
i=5
while (i>0):
    snake.append({"x":30*i,"y":30})
    i-=1
i=0

#SNAKE'S MOVEMENT VARIABLES
ix=30
iy=0

#COLORS
colors=[(230, 149, 183),(255,0,0),(0,255,0),(0,0,255),(147,112,219),
        (255,165,0),(128,128,128),(0,255,255),(255,0,255),(139,69,19)]

for i in range(1,250):
    colors.append(colors[i])

#APPLE'S COORDINATE LIST
level=[]
i=0

while i<810:
    level.append(i)
    i+=30

appleX=rd.choice(level)
appleY=rd.choice(level)

apple2X=rd.choice(level)
apple2Y=rd.choice(level)

#MAIN LOOP
while (loopCont==1):

    #SCALES OF SCREEN
    width=810
    height=810

    #SET THE SCREEN
    wn=pygame.display.set_mode((width,height))

    if not (pygame.mixer.music.get_busy()):
      pygame.mixer.music.load("data\\sound\\Snake.wav")
      pygame.mixer.music.play(-1)

    #QUIT
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        #KEYBOARD CONTROL
        if event.type==pygame.KEYDOWN:
            
            #DOWN
            if event.key==pygame.K_DOWN:
                ix=0
                iy=30
            #UP
            if event.key==pygame.K_UP:
                ix=0
                iy=-30
            #LEFT
            if event.key==pygame.K_LEFT:
                ix=-30
                iy=0
            #RIGHT
            if event.key==pygame.K_RIGHT:
                ix=30
                iy=0
            #STOP
            if event.key==pygame.K_SPACE:
                ix=0
                iy=0

    #CLEAR WINDOW            
    wn.blit(bg,rect)

    #WRITE SCORE
    msg("{}".format(score),70,40,40,140,0,255)

    #DRAW APPLE
    pygame.draw.rect(wn,(255,0,0),[appleX,appleY,30,30])
    pygame.draw.rect(wn,(255,255,0),[apple2X,apple2Y,30,30])

    #EAT 1. APPLE
    if snake[0]["x"]==appleX and snake[0]["y"]==appleY:

        speed=Nspeed
        
        score+=1
        #LOAD APPLE BIT SOUND
        pygame.mixer.music.load("data\\sound\\AppleBit.mp3")
        pygame.mixer.music.play()

        #ADD NEW PIECE
        if ix==30:
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
        elif ix==-30:
            snake.append({"x":snake[len(snake)-1]["x"]+10, "y":snake[len(snake)-1]["y"]})
        elif iy==30:
            snake.append({"x":snake[len(snake)-1]["x"], "y":snake[len(snake)-1]["y"]-10})
        elif iy==-30:
            snake.append({"x":snake[len(snake)-1]["x"], "y":snake[len(snake)-1]["y"]+10})
            
        appleX=rd.choice(level)
        appleY=rd.choice(level)

    #EAT 2. APPLE
    if snake[0]["x"]==apple2X and snake[0]["y"]==apple2Y:

        speed=Hspeed

        score+=2
        #LOAD APPLE BIT SOUND
        pygame.mixer.music.load("data\\sound\\AppleBit.mp3")
        pygame.mixer.music.play()

        #ADD NEW PIECE
        if ix==30:
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
        elif ix==-30:
            snake.append({"x":snake[len(snake)-1]["x"]+10, "y":snake[len(snake)-1]["y"]})
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
        elif iy==30:
            snake.append({"x":snake[len(snake)-1]["x"], "y":snake[len(snake)-1]["y"]-10})
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
        elif iy==-30:
            snake.append({"x":snake[len(snake)-1]["x"], "y":snake[len(snake)-1]["y"]+10})
            snake.append({"x":snake[len(snake)-1]["x"]-10, "y":snake[len(snake)-1]["y"]})
            
        apple2X=rd.choice(level)
        apple2Y=rd.choice(level)

    #DIE
    if (snake[0]["x"])==810 or (snake[0]["x"]+30)==0 or snake[0]["y"]==-30 or snake[0]["y"]==810:
        #LOAD THE SOUND
        stop=1
        pygame.mixer.music.load("data\\sound\\lose.mp3")    
        pygame.mixer.music.play()
        wn.fill((255,200,200))
        wn.blit(rp , rpRect)
        wn.blit(save , saveR)
        pygame.display.flip()
        while stop:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    
                if event.type==pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if rpRect.collidepoint(x,y):
                        stop=0
                        loopCont=0
                        menu1=1
                        menuF(menu1)
                        loopCont=1

                    elif saveR.collidepoint(x,y):
                        scoresTxt=open("data\\score\\scores.txt","a")
                        scoresTxt.write("TIME: {} SCORE: {}\n".format(datetime.datetime.now(),score))
                        scoresTxt.close()
                        msg("SAVED",30,650,555,0,0,255)
                        pygame.display.flip()
        
        while (len(snake)!=0):
            snake.pop()
        i=5

        ix=30
        iy=0
        score=0
        speed=Nspeed
        
        while (i>0):
            snake.append({"x":30*i,"y":30})
            i-=1
    
    #MOVE SNAKE
    sin=len(snake)-1

    while sin>-1:

        if sin!=0:
            snake[sin]["x"]=snake[sin-1]["x"]
            snake[sin]["y"]=snake[sin-1]["y"]
        else:
            snake[sin]["x"]+=ix
            snake[sin]["y"]+=iy

        #DRAW SNAKE RECTS
        pygame.draw.rect(wn,colors[sin],[(snake[sin]["x"]),(snake[sin]["y"]),30,30])

        sin-=1   

    #REFRESH
    pygame.display.flip()

    #FPS       
    clock.tick(speed)
