import pygame
import random
import sys
width = 700
height = 580
gray = (180,180,180)
black = (0,0,0)
PLAY_TIME = 30
size = [width, height]
screen = pygame.display.set_mode(size)
WHITE = (255,255,255)
win = False

def draw_timer(screen, x, y, time_left):
    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render("Time Left = " + str(time_left), 1, WHITE)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.rect.x = width/2
        self.rect.y = 100

    def update(self):
        self.change_y = 3
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        if self.rect.y >= width - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = height - self.rect.height




    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0



class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height,x):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.r = width
        self.image.fill(gray)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 580

        self.change_y = 0

    def update(self):
        self.rect.y -= 3
        if self.rect.y < 0:
            self.kill()



def main():
    global win
    pygame.init()
    screen.fill(black)
    start_time = pygame.time.get_ticks()
    pygame.display.set_caption("Falling_ball")
    done = False
    block_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()

    for i in range(2):
        width1 = random.randint(50, 100)
        height1 = 10

        block = Platform(width1,height1,width/2)
        block_list.add(block)

    player = Player()
    player.update()
    player_list.add(player)
    clock = pygame.time.Clock()



    while not done:
        time_left = pygame.time.get_ticks() - start_time  # find out how much time has passed since the start of the game
        time_left = time_left / 1000  # Convert this time from milliseconds to seconds
        time_left = PLAY_TIME - time_left  # Find out how much time is remaining by subtracting total time from time thats passed
        time_left = int(time_left)  # Convert this value to an integer
        draw_timer(screen, 50, 450, time_left)

        if (start_time + (PLAY_TIME * 1000) <= pygame.time.get_ticks()):
            # If the time is up, set the boolean game_ended to True
            # so we can display the correct game over screen
            win = True
            print(win)
            sys.exit()

        if player.rect.y> height:
            win = False
            print(win)
            sys.exit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = False
                print(win)
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        if len(block_list)< 3:
            width1 = random.randint(0, 200)
            height1 = 10
            block1 = Platform(width1, height1,random.randint(350,width))
            block2 = Platform(width1, height1, random.randint(0, 350))
            block_list.add(block1)
            block_list.add(block2)

        block_list.update()
        collide_list = pygame.sprite.spritecollide(player, block_list, False)
        if len(collide_list) != 0:
            player.rect.bottom -= 2
            player.rect.y -= 6

        player_list.update()
        screen.fill(black)
        draw_timer(screen, 50, 50, time_left)

        player_list.draw(screen)
        block_list.draw(screen)
        clock.tick(60)
        pygame.display.update()


main()
