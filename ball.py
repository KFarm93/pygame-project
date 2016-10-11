import pygame

class Ball(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = radius
        self.color = color

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > width:
            self.speed_x = -5
        if self.y + self.radius > height:
            self.speed_y = -5
        if self.x - self.radius < 0:
            self.speed_x = 5
        if self.y - self.radius < 0:
            self.speed_y = 5

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    ball_list = [
        Ball(50, 50, (255, 0, 0), 50),
        Ball(200, 50, (0, 255, 0), 75),
        Ball(50, 200, (0, 0, 255), 100),
        Ball(50, 300, (255, 255, 0), 75),
        Ball(300, 50, (0, 255, 255), 50)
    ]

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
        for ball in ball_list:
            ball.update(width, height)


        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        ball_list[0].render(screen)
        ball_list[1].render(screen)
        ball_list[2].render(screen)
        ball_list[3].render(screen)
        ball_list[4].render(screen)


        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
