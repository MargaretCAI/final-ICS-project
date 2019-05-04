
import pygame
import random
# -- Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
BLUE = (50, 50, 255)
# Screen dimensions
width = 800
height = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y


    def update(self):
        """ Update the player position. """

        self.rect.x += self.change_x

        if self.rect.x<0:
            self.rect.x = 0
        if self.rect.x > width:
            self.rect.x = width-10
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > height:
            self.rect.y = height


        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


pygame.init()
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


for i in range(0,4):
    wall1 = Wall(20 * i, height-100, 10, 200)
    wall2 = Wall(0, height-20*i, 100, 10)

    wall3 = Wall(0,100*i, width-random.randint(0,width), 10)
    wall4 = Wall(random.randint(50,160), 100 *i +40, random.randint(50,width), 10)


    wall_list.add(wall1)
    wall_list.add(wall2)
    wall_list.add(wall3)
    wall_list.add(wall4)


for i in wall_list:
    all_sprite_list.add(i)







# Create the player paddle object
player = Player(20, 50)
player.walls = wall_list

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False


while not done:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        player.changespeed(0.5, 0)
    if keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        player.changespeed(-0.5, 0)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:


            if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                player.changespeed(0, 5)
            elif event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                player.changespeed(0, -5)

            elif event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)


        elif event.type == pygame.KEYUP:


            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)


    all_sprite_list.update()
    screen.fill(BLACK)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()