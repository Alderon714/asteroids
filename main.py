# this allows us to use code from open-source pygame library throughout this file
#
# Daniel S Cochran
# November 19, 2024
#
import sys
import pygame
from constants import * # import everything from the constants.py file/module
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # allows for milosecond pause in CPU usage.
    dt = 0 # Delta Time
    running = True

    # Groups of objects/actions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # from Pygame documentation https://www.pygame.org/docs/index.html 
    player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() / 2)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running: # infinate loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
#        dt = clock.get_time() / 1000 # calc time in delta time in seconds
        for thing in updatable:
            thing.update(dt)
#       player.update(dt) <-- orginal update Player

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        # RENDER YOUR GAME HERE
        # fil the screen with a color to wipe away anything from last frame
        screen.fill("teal") # teal works! Go Chants
        for thing in drawable:
            thing.draw(screen)
#       player.draw(screen) <-- orginal draw Player
        # flip() the display to put your work on the screen
        pygame.display.flip()

        # limits FPS to 60
#        clock.tick(60)
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
