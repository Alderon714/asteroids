# this allows us to use code from 
# open-source pygame library
# throughout this file
#
# Daniel S Cochran
# Never 19, 2024
#
import pygame
from constants import * # import everything from the constants.py file/module

def main():
    print(f"Starting asteroids!")
    print(f"Screen width:",SCREEN_WIDTH)
    print(f"Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    


if __name__ == "__main__":
    main()
