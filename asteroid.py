# create Asteroid via CircleShape via Sprite in Pygame
import pygame
from circleshape import CircleShape

#NOTE: To create this and override stuff in CircleShape correctly you have to 
#       put all the functions inside of the "class" stuff ie. indent it all dummy! 
#       *Lesson learned* from Player class 
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    