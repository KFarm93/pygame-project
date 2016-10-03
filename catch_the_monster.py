import pygame
import time

class Enemy(object):
    def __init__(self, name, x, y, speed_x, speed_y):
        self.name = name
        self.x = x
        self.y = y

class Monster(Enemy):
    def __init__(self):
        self.name = monster
        self.x = monster_x
        self.y = monster_y
        self.speed_x = 5

    def update(self):
        self.x += self.speed_x

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

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
    hero = pygame.image.load('images/hero.png').convert_alpha()
    monster = pygame.image.load('images/monster.png').convert_alpha()
    hero_x = 250
    hero_y = 250
    monster_x = 150
    monster_y = 150


    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        # fill background color
        screen.fill(blue_color)
        screen.blit(backgroundImg, (0, 0))
        screen.blit(hero, (hero_x, hero_y))
        screen.blit(monster, (monster_x, monster_y))
        if monster_x < 512:
            monster_x += 5
        else:
            monster_x = 0




        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
