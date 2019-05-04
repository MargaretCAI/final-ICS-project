import random
import pygame
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Classes


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])

        self.rect = self.image.get_rect()
        color = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
        self.image.fill(color)

    def update(self):

        self.rect.y -= 3


def main():
    pygame.init()

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode([screen_width, screen_height])

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

    done = False
    clock = pygame.time.Clock()
    score = 0
    player.rect.y = 370


    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

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
                sound = pygame.mixer.Sound('beep.wav').play()
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



main()
