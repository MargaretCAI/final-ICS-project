
import pygame
import random
PLAY_TIME = 30
background_image = pygame.image.load("image/grass03.png")

SIZE = WIDTH, HEIGHT = 900, 700  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('black')
# The background colod of our window
FPS = 40  # Frames per second
WHITE=(255,255,255)

def draw_timer(screen, x, y, time_left):
    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render("Time Left = " + str(time_left), 1, WHITE)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen

def draw_score(screen, x, y, score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score = " + str(score), 1, WHITE)
    screen.blit(text, (x, y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('image/walk1.png'))
        self.images.append(pygame.image.load('image/walk2.png'))
        self.images.append(pygame.image.load('image/walk3.png'))
        self.images.append(pygame.image.load('image/walk4.png'))
        self.images.append(pygame.image.load('image/walk5.png'))
        self.images.append(pygame.image.load('image/walk6.png'))
        # self.images.append(pygame.image.load('images/walk7.png'))
        # self.images.append(pygame.image.load('images/walk8.png'))
        # self.images.append(pygame.image.load('images/walk9.png'))
        # self.images.append(pygame.image.load('images/walk10.png'))

        self.index = 0

        self.image = self.images[self.index]


        #self.rect = pygame.Rect(5, 5, 150, 198)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.index += 1
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.index >= len(self.images):
            self.index = 0


        self.image = self.images[self.index]

    def go_left(self):
        self.change_x = -10

    def go_right(self):
        self.change_x = 10

    def go_up(self):
        self.change_y = -10

    def go_down(self):
        self.change_y = 10


    def stop(self):
        self.change_x = 0
        self.change_y = 0



class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('image/star.png'))
        self.images.append(pygame.image.load('image/star2.png'))
        self.images.append(pygame.image.load('image/star.png'))
        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('image/gold_1.png'))
        self.images.append(pygame.image.load('image/gold_2.png'))
        self.images.append(pygame.image.load('image/gold_3.png'))
        self.images.append(pygame.image.load('image/gold_4.png'))
        self.images.append(pygame.image.load('image/gold_5.png'))
        self.images.append(pygame.image.load('image/gold_6.png'))




        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH)
        self.rect.y = random.randint(0, HEIGHT)



    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        # self.image = pygame.transform.scale(self.image, (20, 40))



def main():
    score = 0
    pygame.init()
    start_time = pygame.time.get_ticks()

    screen = pygame.display.set_mode(SIZE)
    player = Player()
    coin_list = pygame.sprite.Group()
    star_list = pygame.sprite.Group()

    for i in range(0,40):

        coin = Coin()
        coin_list.add(coin)



    player_list = pygame.sprite.Group(player)

    clock = pygame.time.Clock()

    while True:


        for i in coin_list:
            if i.rect.collidepoint(player.rect.x+45, player.rect.y+40):
                coin_list.remove(i)
                score += 10
        for i in star_list:
            if i.rect.collidepoint(player.rect.x+45, player.rect.y+40):
                star_list.remove(i)
                score += 10

        time_left = pygame.time.get_ticks() - start_time  # find out how much time has passed since the start of the game
        time_left = time_left / 1000  # Convert this time from milliseconds to seconds
        time_left = PLAY_TIME - time_left  # Find out how much time is remaining by subtracting total time from time thats passed
        time_left = int(time_left)  # Convert this value to an integer
        draw_timer(screen, 50, 450, time_left)

        if (start_time + (PLAY_TIME * 1000) <= pygame.time.get_ticks()):
            # If the time is up, set the boolean game_ended to True
            # so we can display the correct game over screen
            win = 0
            pygame.quit()
            print(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()

        draw_timer(screen, 50, 50, time_left)
        player_list.update()
        coin_list.update()
        star_list.update()
        screen.fill(BACKGROUND_COLOR)

        player_list.draw(screen)
        draw_score(screen, 100, 100, score)
        coin_list.draw(screen)
        star_list.draw(screen)
        draw_timer(screen, 50, 50, time_left)

        pygame.display.update()

        clock.tick(50)
        if (time_left < 25):
            for i in coin_list:
                coin_list.remove(i)

        if time_left == 23:
            for i in range(0, 1):
                star = Star()
                star_list.add(star)


if __name__ == '__main__':
    main()