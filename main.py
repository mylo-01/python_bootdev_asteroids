# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from  constants import *
from player import Player
from circle_shape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    ### Create groups():
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group, )
    Shot.containers = (shots, updatable_group, drawable_group)

    ### Create field instance
    field = AsteroidField()

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
        updatable_group.update(dt)
        # player01.update(dt) NOT NECESARY ANYMORE
        # player01.draw(screen) NOT NECESARY ANYMORE
        for drawable_object in drawable_group:
            drawable_object.draw(screen)
        # Shots...


        for asteroid in asteroids:
            if player01.check_collision(asteroid):
                print("Game over!")
                sys.exit() 

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        ## render phisical screen
        pygame.display.flip()
        ## limit fps
        dt = clock.tick(60) / 1000
        ## Check for colissions
if __name__ == "__main__":
    main()
