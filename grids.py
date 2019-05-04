

import pygame, random, sys
from pygame.locals import *
import wormy
import bouncing_ball
import hit_the_plane

FPS = 15
width = 640
height = 480
# cellsize = 20
# assert width%cellsize == 0
# assert height%cellsize == 0
# cellwidth = int(width/cellsize)
# cellheight = int(height/cellsize)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
darkgray = (0,150,100)
background = black
head = 0
clock = pygame.time.Clock()
introduction = True




def intro(introduction):

    pygame.init()
    DISPLAY = pygame.display.set_mode((width, height), 0, 32)

    WHITE = (255, 255, 255)
    blue = (135, 206, 250)

    yellow = (255, 255, 0)
    size = 90
    xoffset = 100
    yoffset = 10

    DISPLAY.fill(WHITE)
    i = 1
    Rectplace1 = pygame.draw.rect(DISPLAY, blue, (xoffset, yoffset + i * size, size, size))
    Rectplace2 = pygame.draw.rect(DISPLAY, yellow, (xoffset + size, yoffset + i * size, size, size))
    Rectplace3 = pygame.draw.rect(DISPLAY, blue, (xoffset + 2 * size, yoffset + i * size, size, size))
    i = 2
    Rectplace4 = pygame.draw.rect(DISPLAY, yellow, (xoffset, yoffset + i * size, size, size))
    Rectplace5 = pygame.draw.rect(DISPLAY, blue, (xoffset + size, yoffset + i * size, size, size))
    Rectplace6 = pygame.draw.rect(DISPLAY, yellow, (xoffset + 2 * size, yoffset + i * size, size, size))

    i = 3
    Rectplace7 = pygame.draw.rect(DISPLAY, blue, (xoffset, yoffset + i * size, size, size))
    Rectplace8 = pygame.draw.rect(DISPLAY, yellow, (xoffset + size, yoffset + i * size, size, size))
    Rectplace9 = pygame.draw.rect(DISPLAY, blue, (xoffset + 2 * size, yoffset + i * size, size, size))

    while introduction:

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()

        if Rectplace1.collidepoint(pos) and pressed1:
            print("clicked!")
            wormy.main()

        elif Rectplace2.collidepoint(pos) and pressed1:
            print("clicked2!")
            bouncing_ball.main()

        elif Rectplace3.collidepoint(pos) and pressed1:
            print("clicked3!")
            hit_the_plane.main()



intro(introduction)






