import pygame
import time
from random import randint
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def sqr(x):
    return x * x

def distance(a, b):
    return math.sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))

class Enemy(object):
    def __init__(self, x, y, speed_x, speed_y):
        self.name = name
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

class Monster(Enemy):
    def __init__(self):
        self.x = 300
        self.y = 170
        self.speed_x = 5
        self.speed_y = 5
        self.img = pygame.image.load('images/monster.png').convert_alpha()
        self.change_dir_countdown = 120

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > 512:
            self.x = 0
        if self.y > 480:
            self.y = 0
        if self.x < 0:
            self.x = 512
        if self.y < 0:
            self.y = 480

        now = time.time()
        self.change_dir_countdown -= 2
        if self.change_dir_countdown == 0:
            num = randint(0, 4)
            self.change_dir_countdown = 60
            if num == 0:
                self.speed_x = 5
                self.speed_y = 0
            elif num == 1:
                self.speed_x = -5
                self.speed_y = 0
            elif num == 2:
                self.speed_y = 5
                self.speed_x = 0
            else:
                self.speed_y = -5
                self.speed_x = 0

    def respawn(self):
        self.x = 1
        self.y = 1
        self.speed_x = 0
        self.speed_y = 0


class Hero(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.speed_x = 0
        self.speed_y = 0
        self.img = pygame.image.load('images/hero.png').convert_alpha()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > 452:
            self.x = 452
        if self.y > 420:
            self.y = 420
        if self.x < 20:
            self.x = 20
        if self.y < 20:
            self.y = 20

    def collision(self, monster):
        return distance(self, monster) < 32

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    count = 0




    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    backgroundImg = pygame.image.load('images/background.png').convert_alpha()
    win_sound = pygame.mixer.Sound('sounds/win.wav')

    monster = Monster()
    hero = Hero()

    # game loop
    game_over = False
    stop_game = False
    while not stop_game:






        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_DOWN:
                        hero.speed_y = 4
                    elif event.key == KEY_UP:
                        hero.speed_y = -4
                    elif event.key == KEY_LEFT:
                        hero.speed_x = -4
                    elif event.key == KEY_RIGHT:
                        hero.speed_x = 4
                if event.type == pygame.KEYUP:
                    if event.key == KEY_DOWN:
                        hero.speed_y = 0
                    elif event.key == KEY_UP:
                        hero.speed_y = 0
                    elif event.key == KEY_LEFT:
                        hero.speed_x = 0
                    elif event.key == KEY_RIGHT:
                        hero.speed_x = 0
            ################################
        if not game_over:
            monster.update()
            hero.update()
            if hero.collision(monster):
                win_sound.play()
                game_over = True




            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        # fill background color
            screen.blit(backgroundImg, (0, 0))
            screen.blit(hero.img, (hero.x, hero.y))
            screen.blit(monster.img, (monster.x, monster.y))







        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        if game_over:
            font = pygame.font.Font(None, 40)
            text = font.render("Hit 'ENTER' to play again!", True, (0,0,0))
            screen.blit(text, (80, 230))
        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
