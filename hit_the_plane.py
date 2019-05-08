import random
import pygame
import sys

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
win = False
pygame.init()
WIDTH = 480
HEIGHT = 600
font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def main_menu():
    text1 = "Press [ENTER] To Begin"
    global screen
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode([screen_width, screen_height])

    title = pygame.image.load("ball.png")
    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        # screen.blit(title,(200,200))
        draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "or [Q] To Quit", 30, WIDTH / 2, (HEIGHT / 2) + 40)
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()

        elif ev.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
    main()






class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1



class Block(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("apple.png")
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = HEIGHT




class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.y -= 3
        if self.rect.top > HEIGHT:
            self.kill()


def main():
    pygame.init()
    global win
    done = False
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(WHITE)
    block_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()

    for i in range(4):
        # This represents a block
        block = Block(BLUE)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = 0

        # Add the block to the list of objects
        block_list.add(block)

    # Create a red player block
    player = Player()
    player_list.add(player)

    clock = pygame.time.Clock()
    score = 0
    player.rect.y = 370


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = False
                done = True
                print(win)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                    bullet_list.add(bullet)

        if len(block_list) < 30:
            for i in range(3):
                # This represents a block
                block = Block(BLUE)

                # Set a random location for the block
                block.rect.x = random.randrange(screen_width)
                block.rect.y = 0

                # Add the block to the list of objects
                block_list.add(block)
            else:
                pass

        # Call the update() method on all the sprites
        block_list.update()
        bullet_list.update()
        player_list.update()

        # Calculate mechanics for each bullet
        for bullet in bullet_list:

            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                # sound = pygame.mixer.Sound('beep.wav').play()
                bullet_list.remove(bullet)

                score += 1
                print(score)

            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)

        for block in block_list:
            if block.rect.y > screen_height:
                block_list.remove(block)



        screen.fill(WHITE)

        bullet_list.draw(screen)
        block_list.draw(screen)
        player_list.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


main_menu()

