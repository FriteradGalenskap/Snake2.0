
import pygame
from threading import Thread

import random
import sys
from typing import Tuple
import time
height = 200
width = 200
SCREEN_SIZE = (height, width)
FRAME_RATE = 30
SCORE = 0

boxLenth= int(height*1/100)
padding = boxLenth   
direction=0
 
lineW = width - padding
lineH = height - padding


def init() -> Tuple[pygame.Surface, pygame.time.Clock]:
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Window")
    clock = pygame.time.Clock()

    return screen, clock



   
    
    
def draw(screen, xCor,yCor,Col):
    r = pygame.Rect(xCor,yCor,boxLenth,boxLenth)
    
    pygame.draw.rect(screen, Col, r)
    #print(f"x: {xCor}, y: {yCor}")
    
def calcNxtBox(X,Y,D):
    if D==0:
        X += boxLenth
    elif D==1:
        Y += boxLenth
    elif D==2:
        X-= boxLenth
    else:
        Y -=boxLenth
    return (X,Y)

    
def frame(screen):
    size = 5
    pygame.draw.line(screen,'white',(padding,padding),(lineW,padding),size)
    pygame.draw.line(screen,'white',(padding,padding),(padding,lineH),size)
    pygame.draw.line(screen,'white',(lineW,lineH),(lineW,padding),size)
    pygame.draw.line(screen,'white',(lineW,lineH),(padding,lineH),size)
    
def collisionDetection(x,y):
    return x>=lineW or x<padding or y>=lineH or y<padding



    pass
class Apple:
    def listCords(self):
        
        print(f'x{self.x}y{self.y}')
    def __init__(self):
        self.x=random.randint(int(1+(padding/boxLenth)) ,int((lineW/boxLenth)-1))*boxLenth
        self.y=random.randint(int(1+(padding/boxLenth)),int((lineH/boxLenth)-1))*boxLenth
        #self.listCords()

class Box:
    x=0
    y=0
    def __init__(self, x, y):
        self.x =x
        self.y=y

class Snake:
    
    boxar=[]
    def __init__(self):
        pass

def main(screen: pygame.Surface, clock: pygame.time.Clock):
    appleHit=False
    global FRAME_RATE
    global SCORE
    frame(screen)
    apple = Apple()
    draw(screen,apple.x,apple.y,'red')
    snake=Snake()

    yMid = int(height/2)
    xMid = int(width/2)
    box1 = Box(xMid,yMid)
    box2 = Box(xMid-boxLenth,yMid)
    box3 = Box(xMid-2*boxLenth,yMid)
    box4 = Box(xMid-3*boxLenth,yMid)
    snake.boxar.append(box1)
    snake.boxar.append(box2)
    snake.boxar.append(box3)
    snake.boxar.append(box4)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        boxFront = snake.boxar[0]
        box2 = snake.boxar[1]
        box3 = snake.boxar[2]
        box4 = snake.boxar[3]
        boxDirection = direction
        newBox= calcNxtBox(boxFront.x,boxFront.y,boxDirection)
       
        box =Box(newBox[0],newBox[1])
        snake.boxar.insert(0,box)
        draw(screen,newBox[0],newBox[1],'red')
        appleHit = apple.x == newBox[0] and apple.y == newBox[1]
        if collisionDetection(newBox[0],newBox[1]):
            time.sleep(2638476243)
        if not appleHit:
            l = len(snake.boxar)
            boxBack = snake.boxar[l-1]
            snake.boxar.pop(l-1)
            draw(screen,boxBack.x,boxBack.y,'black')
            #print(f"anal boxar: {l}")
        else:
            apple=Apple()
            draw(screen,apple.x,apple.y,'red')
            FRAME_RATE+=1
            SCORE += 1 
            print(SCORE)


        pygame.display.update()
        clock.tick(FRAME_RATE)

def keyListener():
    global direction 
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 2
                elif event.key == pygame.K_RIGHT:
                    direction = 0
                elif event.key == pygame.K_DOWN:
                    direction = 1
                elif event.key == pygame.K_UP:
                    direction =3   

if __name__ == "__main__":
    screen, clock = init()
    from threading import Thread
    t = Thread(target=keyListener)
    t.start()
    main(screen, clock)
    
