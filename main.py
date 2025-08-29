# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from  constants import *

#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    #print("Hello from python-bootdev-asteroids!")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    ###
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    i = 1
    while i == 1:
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
