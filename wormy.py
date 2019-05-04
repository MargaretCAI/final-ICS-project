import pygame, random, sys
from pygame.locals import *

FPS = 15
width = 640
height = 480
cellsize = 20
assert width % cellsize == 0
assert height % cellsize == 0
cellwidth = int(width / cellsize)
cellheight = int(height / cellsize)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkgray = (0, 150, 100)
background = black
head = 0
clock = pygame.time.Clock()
introduction = True


def main():
    global displaysurface
    global clock
    pygame.init()
    displaysurface = pygame.display.set_mode((width, height))

    pygame.display.set_caption("wormy!")
    showStartScreen()
    while True:
        runGame()
        # showGameOver()


def foodlocation():
    return {"x": random.randint(0, cellwidth - 2), "y": random.randint(0, cellheight - 2)}


def runGame():
    direction = "right"

    startx = random.randint(5, cellwidth - 6)
    starty = random.randint(6, cellheight - 6)
    wormCoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty},
                  {'x': startx - 3, 'y': starty},
                  {'x': startx - 4, 'y': starty}
                  ]

    food = foodlocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = "left"
                elif event.key == K_RIGHT:
                    direction = "right"
                elif event.key == K_UP:
                    direction = "up"
                elif event.key == K_DOWN:
                    direction = "down"

        if wormCoords[head]['x'] == -1:
            wormCoords[head]['x'] = cellwidth

        elif wormCoords[head]['x'] == cellwidth:
            wormCoords[head]['x'] = -1

        elif wormCoords[head]['y'] == cellheight:
            wormCoords[head]['y'] = -1

        elif wormCoords[head]['y'] == -1:
            wormCoords[head]['y'] = cellheight

        # check apple and collision

        if wormCoords[0]["x"] == food["x"] and wormCoords[0]["y"] == food["y"]:
            food = foodlocation()
            length = len(wormCoords) - 1
            newtail = {"x": wormCoords[length]['x'], "y": wormCoords[length]["y"]}
            wormCoords.insert(length, newtail)

        # checkgameover
        for body in wormCoords[1:]:
            if body["x"] == wormCoords[0]["x"] and body["y"] == wormCoords[0]["y"]:
                terminate()

        if direction == "up":
            newHead = {"x": wormCoords[0]['x'], "y": wormCoords[0]["y"] - 1}
        elif direction == "right":
            newHead = {"x": wormCoords[0]['x'] + 1, "y": wormCoords[0]["y"]}

        elif direction == "down":
            newHead = {"x": wormCoords[0]['x'], "y": wormCoords[0]["y"] + 1}
        elif direction == "left":
            newHead = {"x": wormCoords[0]['x'] - 1, "y": wormCoords[0]["y"]}

        wormCoords.insert(0, newHead)
        wormCoords.pop()
        displaysurface.fill(black)

        drawWorm(wormCoords)
        drawfood(food)
        pygame.display.update()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def drawfood(coord):
    x = coord["x"] * cellsize
    y = coord["y"] * cellsize
    foodrect = pygame.Rect(x, y, cellsize, cellsize)
    pygame.draw.rect(displaysurface, red, foodrect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * cellsize
        y = coord['y'] * cellsize
        wormrect = pygame.Rect(x, y, cellsize, cellsize)
        pygame.draw.rect(displaysurface, green, wormrect)
        worminnerrect = pygame.Rect(x + 3, y + 3, cellsize - 9, cellsize - 9)
        pygame.draw.rect(displaysurface, green, worminnerrect)


def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                return True


def showStartScreen():
    titleFont = pygame.font.Font("freesansbold.ttf", 100)
    font1 = titleFont.render("Wormy!", True, white, darkgray)
    degree1 = 0
    while True:
        displaysurface.fill(background)
        rotatefont1 = pygame.transform.rotate(font1, degree1)
        rotateRect1 = rotatefont1.get_rect()
        rotateRect1.center = (width / 2, height / 2)
        displaysurface.blit(rotatefont1, rotateRect1)
        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        clock.tick(FPS)
        degree1 += 3

main()


