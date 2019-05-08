import pygame
from random import randint
import sys

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
size = 640, 560
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy_Bird")
background_image = pygame.image.load("background_bird.png")
gray = (160,160,160)
dark_gray = (96,96,96)
done = False
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0, 350)
space = 150
obspeed = 2.5
score = 0
gravity = 1
win = False
PLAY_TIME = 30



def draw_timer(screen, x, y, time_left):
    font = pygame.font.Font(None, 35)  # Choose the font for the text
    text = font.render("Time Left = " + str(time_left), 1, black)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen




def draw_stick_figure(screen, x, y, colour, scale):

    pygame.draw.ellipse(screen, BLACK, [int(1 * scale) + x, y, int(10 * scale), int(10 * scale)], 0)

    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y],
                     [int(10 * scale) + x, int(27 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y], [x, int(27 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(17 * scale) + y],
                     [int(5 * scale) + x, int(7 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(7 * scale) + y],
                     [int(9 * scale) + x, int(17 * scale) + y], int(2 * scale))
    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(7 * scale) + y],
                     [int(1 * scale) + x, int(17 * scale) + y], int(2 * scale))



def gameover():
    font = pygame.font.SysFont(None, 75)
    text = font.render("Game over", True, red)
    screen.blit(text, [150, 250])

def Score(score):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])


def main(xloc,ysize,score,y_speed,obspeed,y,gravity,done=False):

    start_time = pygame.time.get_ticks()

    global win
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = True
                print(win)
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_speed = -10

                if event.key == pygame.K_p:
                    pygame.time.wait(3000)
                    pygame.mouse.set_visible(0)

                    pass


        time_left = pygame.time.get_ticks() - start_time
        time_left = time_left / 1000
        time_left = PLAY_TIME - time_left
        time_left = int(time_left)


        screen.blit(background_image, (0, 0))
        y_speed += gravity
        pygame.draw.rect(screen, gray, [xloc, yloc, xsize, ysize])
        pygame.draw.rect(screen, dark_gray, [xloc-5, yloc, 5, ysize])
        pygame.draw.rect(screen, dark_gray, [xloc+xsize, yloc, 5, ysize])
        pygame.draw.rect(screen, gray, [xloc, int(yloc + ysize + space), xsize, ysize + 500])
        pygame.draw.rect(screen, dark_gray, [xloc-5, int(yloc + ysize + space), 5, ysize + 500])
        draw_stick_figure(screen, x, y, red, 1.2)


        Score(score)

        y += y_speed
        xloc -= obspeed
        if y > ground:
            y = 0
        if y< 0:
            y = ground

        if x + 20 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if x + 20 > xloc and y + 20 > ysize + space and x - 15 < xsize + xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if xloc < -80:
            xloc = 700
            ysize = randint(0, 350)

        if x > xloc and x < xloc + 3:
            score = score + 1

        draw_timer(screen, 10, 50, time_left)

        pygame.display.update()
        clock.tick(80)

main(xloc,ysize,score,y_speed,obspeed,y,gravity)

