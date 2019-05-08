import pygame
import random
color = (200, 100, 50)
pygame.init()
width = 600
height = 480
black = (0,0,0)
white = (255,255,255)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = False
FPS = 60
background_image = pygame.image.load('snow.jpg').convert()

def main():
    global screen
    global clock
    pygame.init()
    pygame.display.set_caption("snow")
    showStartScreen()

    while True:
        running()


def showStartScreen():
    titleFont = pygame.font.Font("freesansbold.ttf", 50)
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    font1 = titleFont.render("Bonus!", True, white, color)
    text = "Congrats!This is a block that does not require playing a game!"
    text2 = "Just enjoy the music and beautiful snow for 10 seconds!"


    textsurface = myfont.render(text, False, white)
    textsurface2 = myfont.render(text2, False, white)


    degree1 = 0
    while True:
        screen.fill(black)
        for i in range(0,10):

            pygame.draw.line(screen,color,(random.randint(60, 120),random.randint(0, height/1.5)),
                             (random.randint(60, 120), random.randint(0, height/1.5)),random.randint(0, 5))
            pygame.draw.line(screen, color, (random.randint(120, 180), random.randint(0, height / 1.5)),
                             (random.randint(120, 180), random.randint(0, height / 1.5)), random.randint(0, 5))
            pygame.draw.line(screen, color, (random.randint(180, 240), random.randint(0, height / 1.5)),
                             (random.randint(180, 240), random.randint(0, height / 1.5)), random.randint(0, 5))




        rotatefont1 = pygame.transform.scale(font1,(200,100))


        rotateRect1 = rotatefont1.get_rect()
        screen.blit(textsurface, (20, height-200))
        screen.blit(textsurface2, (20, height - 150))

        rotateRect1.center = (width / 2, height / 4)

        screen.blit(rotatefont1, rotateRect1)
        if checkForKeyPress():
            return

        pygame.display.update()
        clock.tick(FPS)
        degree1 += 3



def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True


def running():


    snow = []
    for i in range(0, 90):
        snow_x = random.randrange(0, width)
        snow_y = random.randrange(0, height)
        snow.append([snow_x, snow_y])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(background_image, [0, 0])

        for i in snow:
            i[1] += 1
            pygame.draw.circle(screen, white, i, 7)

            if i[1] > 580:
                i[1] = random.randrange(-50, -5)
                i[0] = random.randrange(0, width)

        pygame.display.flip()
        clock.tick(FPS)

main()





