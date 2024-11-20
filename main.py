# this allows us to use code from open-source pygame library throughout this file
#
# Daniel S Cochran
# November 19, 2024
#
import pygame
from constants import * # import everything from the constants.py file/module
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # allows for milosecond pause in CPU usage.
    dt = 0 # Delta Time
    running = True

    # from Pygame documentation https://www.pygame.org/docs/index.html 
    player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() / 2)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running: # infinate loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
#        dt = clock.get_time() / 1000 # calc time in delta time in seconds
        player.update(dt)

        # RENDER YOUR GAME HERE
        # fil the screen with a color to wipe away anything from last frame
        screen.fill("teal") # teal works! Go Chants
        player.draw(screen)
        # flip() the display to put your work on the screen
        pygame.display.flip()

        # limits FPS to 60
#        clock.tick(60)
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
