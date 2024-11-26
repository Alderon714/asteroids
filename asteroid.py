# create Asteroid via CircleShape via Sprite in Pygame
import pygame
import random
from circleshape import CircleShape
from constants import *

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # random angle of the new asteriods from the original
        angle_of = random.uniform(20, 50)

        a = self.velocity.rotate(angle_of)
        b = self.velocity.rotate(-angle_of)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

    