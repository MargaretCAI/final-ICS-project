import pygame
import random
width = 700
height = 580
gray = (180,180,180)
black = (0,0,0)

size = [width, height]
screen = pygame.display.set_mode(size)

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
        self.change_y = 1
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
        self.image.fill(gray)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 580

        self.change_y = 0

    def update(self):
        self.rect.y -= 3
        if self.rect.y < -10:
            self.kill()



def main():
    pygame.init()
    screen.fill(black)
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

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
        if len(block_list)< 1:
            width1 = random.randint(0, 200)
            height1 = 10
            block1 = Platform(width1, height1,random.randint(350,width))
            block2 = Platform(width1, height1, random.randint(0, 350))
            block_list.add(block1)
            block_list.add(block2)
        else:
            pass


        block_list.update()
        player_list.update()
        screen.fill(black)
        player_list.draw(screen)
        block_list.draw(screen)
        clock.tick(60)
        pygame.display.update()


main()
#
# import pygame
# from pygame.locals import *
#
#
# class MySprite(pygame.sprite.Sprite):
#     def __init__(self, target):
#         pygame.sprite.Sprite.__init__(self)
#         self.target_surface = target
#         self.image = None
#         self.master_image = None
#         self.rect = None
#         self.topleft = 0, 0
#         self.frame = 0
#         self.old_frame = -1
#         self.frame_width = 1
#         self.frame_height = 1
#         self.first_frame = 0
#         self.last_frame = 0
#         self.columns = 1
#         self.last_time = 0
#
#     def load(self, filename, width, height, columns):
#         self.master_image = pygame.image.load(filename).convert_alpha()
#         self.frame_width = width
#         self.frame_height = height
#         self.rect = self.master_image.get_rect()
#         self.columns = columns
#         rect = self.master_image.get_rect()
#         self.last_frame = (rect.width // width) * (rect.height // height) - 1
#
#     def update(self, current_time, rate=60):
#         self.rect.y+=1
#
#
#         if current_time > self.last_time + rate:
#             self.frame += 1
#             if self.frame > self.last_frame:
#                 self.frame = self.first_frame
#             self.last_time = current_time
#
#         if self.frame != self.old_frame:
#             frame_x = (self.frame % self.columns) * self.frame_width
#             frame_y = (self.frame // self.columns) * self.frame_height
#             rect = (frame_x, frame_y, self.frame_width, self.frame_height)
#             self.image = self.master_image.subsurface(rect)
#             self.old_frame = self.frame
#
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600), 0, 32)
# pygame.display.set_caption("精灵类测试")
# font = pygame.font.Font(None, 18)
# framerate = pygame.time.Clock()
#
# cat = MySprite(screen)
# cat.load("sprite.png", 100, 100, 4)
# group = pygame.sprite.Group()
# group.add(cat)
#
# while True:
#     framerate.tick(30)
#     ticks = pygame.time.get_ticks()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     key = pygame.key.get_pressed()
#     if key[pygame.K_ESCAPE]:
#         exit()
#
#     screen.fill((0, 0, 100))
#
#     group.update(ticks)
#     group.draw(screen)
#     pygame.display.update()