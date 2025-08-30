# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from  constants import *
from player import *
from circle_shape import *

#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    #print("Hello from python-bootdev-asteroids!")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ### Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ### Add frame rate
    clock = pygame.time.Clock()
    dt = 0

    ### Initiate Player:
    player01 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    ### Game While loop
    running = True
    while running:
        for event in pygame.event.get():
            ## Close game
            if event.type == pygame.QUIT:
                return
        ## create digital screen
        screen.fill((0,0,0))
        ## render player
        player01.draw(screen)
        ## render phisical screen
        pygame.display.flip()
        ## limit fps
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
