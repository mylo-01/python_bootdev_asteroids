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
    
    ### Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ### Add frame rate
    

    ### Game While loop
    while i == i:
        for event in pygame.event.get():
            ## Close game
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
