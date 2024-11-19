# this allows us to use code from open-source pygame library throughout this file
#
# Daniel S Cochran
# November 19, 2024
#
import pygame
from constants import * # import everything from the constants.py file/module

def main():
    # print(f"Starting asteroids!")
    # print(f"Screen width:",SCREEN_WIDTH)
    # print(f"Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # allows for milosecond pause in CPU usage.
    dt = 0 # Delta Time
    while True: # infinate loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick() / 1000
        # print("delta time:", dt) # that worked *rolls eyes* 

if __name__ == "__main__":
    main()
